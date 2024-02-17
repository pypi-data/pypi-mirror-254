use bstr::Finder;
use once_cell::sync::Lazy;
use pyo3::intern;
use pyo3::prelude::*;
use pyo3::types::PyDict;
use pyo3::types::PyFrame;
use serde::Serialize;
use std::cell::RefCell;
use std::collections::HashMap;

use super::utils;

macro_rules! count {
        // Macro magic to find the length of $path
        // https://youtu.be/q6paRBbLgNw?t=4380
        ($($element:expr),*) => {
            [$(count![@SUBSTR; $element]),*].len()
        };
        (@SUBSTR; $_element:expr) => {()};
    }

macro_rules! finder {
        ($name:ident = $path:expr) => {
            static $name: Lazy<Finder> = Lazy::new(|| Finder::new($path));
        };
        (pub $name:ident = $path:expr) => {
            pub static $name: Lazy<Finder> = Lazy::new(|| Finder::new($path));
        };
        (pub $name:ident = $($path:expr),+ $(,)?) => {
            pub static $name: Lazy<[Finder; count!($($path),*)]> = Lazy::new(|| {
                [
                    $(Finder::new($path),)+
                ]
            });
        };

    }

finder!(CELERY_FINDER = "celery");
finder!(SENTRY_FINDER = "sentry_sdk");
finder!(DJANGO_FINDER = "django");
finder!(FROZEN_FINDER = "<frozen ");
finder!(EXEC_FINDER = "<string>");

#[cfg(target_os = "windows")]
mod windows {
    use bstr::Finder;
    use once_cell::sync::Lazy;
    finder!(pub MIDDLEWARE_FINDER = "\\kolo\\middleware.py");
    finder!(pub DJANGO_CHECKS_FINDER = "django\\core\\checks\\registry.py");
    finder!(pub DJANGO_TEST_DB_FINDER = "django\\db\\backends\\base\\creation.py");
    finder!(pub DJANGO_SETUP_FINDER = "django\\__init__.py");
    finder!(pub TEMPLATE_FINDER = "django\\template\\backends\\django.py");
    finder!(pub HUEY_FINDER = "\\huey\\api.py");
    finder!(pub REQUESTS_FINDER = "requests\\sessions");
    finder!(pub HTTPX_FINDER = "httpx\\_client.py");
    finder!(pub URLLIB_FINDER = "urllib\\request");
    finder!(pub URLLIB3_FINDER = "urllib3\\connectionpool");
    finder!(pub LOGGING_FINDER = "\\logging\\");
    finder!(pub SQL_FINDER = "\\django\\db\\models\\sql\\compiler.py");
    finder!(pub PYTEST_FINDER = "kolo\\pytest_plugin.py");
    finder!(pub UNITTEST_FINDER = "unittest\\result.py");
    finder!(pub LIBRARY_FINDERS = "lib\\python", "\\site-packages\\", "\\x64\\lib\\");
    finder!(pub LOWER_PYTHON_FINDER = "\\python\\");
    finder!(pub UPPER_PYTHON_FINDER = "\\Python\\");
    finder!(pub LOWER_LIB_FINDER = "\\lib\\");
    finder!(pub UPPER_LIB_FINDER = "\\Lib\\");
    finder!(pub KOLO_FINDERS = "\\kolo\\config.py",
        "\\kolo\\db.py",
        "\\kolo\\django_schema.py",
        "\\kolo\\filters\\",
        "\\kolo\\generate_tests\\",
        "\\kolo\\git.py",
        "\\kolo\\__init__.py",
        "\\kolo\\__main__.py",
        "\\kolo\\middleware.py",
        "\\kolo\\profiler.py",
        "\\kolo\\pytest_plugin.py",
        "\\kolo\\serialize.py",
        "\\kolo\\utils.py",
        "\\kolo\\version.py");
}
#[cfg(target_os = "windows")]
use windows::*;

#[cfg(not(target_os = "windows"))]
mod not_windows {
    use bstr::Finder;
    use once_cell::sync::Lazy;
    finder!(pub MIDDLEWARE_FINDER = "/kolo/middleware.py");
    finder!(pub DJANGO_CHECKS_FINDER = "django/core/checks/registry.py");
    finder!(pub DJANGO_TEST_DB_FINDER = "django/db/backends/base/creation.py");
    finder!(pub DJANGO_SETUP_FINDER = "django/__init__.py");
    finder!(pub TEMPLATE_FINDER = "django/template/backends/django.py");
    finder!(pub HUEY_FINDER = "/huey/api.py");
    finder!(pub REQUESTS_FINDER = "requests/sessions");
    finder!(pub HTTPX_FINDER = "httpx/_client.py");
    finder!(pub URLLIB_FINDER = "urllib/request");
    finder!(pub URLLIB3_FINDER = "urllib3/connectionpool");
    finder!(pub LOGGING_FINDER = "/logging/");
    finder!(pub SQL_FINDER = "/django/db/models/sql/compiler.py");
    finder!(pub PYTEST_FINDER = "kolo/pytest_plugin.py");
    finder!(pub UNITTEST_FINDER = "unittest/result.py");
    finder!(pub LIBRARY_FINDERS = "lib/python", "/site-packages/");
    finder!(pub KOLO_FINDERS = "/kolo/config.py",
        "/kolo/db.py",
        "/kolo/django_schema.py",
        "/kolo/filters/",
        "/kolo/generate_tests/",
        "/kolo/git.py",
        "/kolo/__init__.py",
        "/kolo/__main__.py",
        "/kolo/middleware.py",
        "/kolo/profiler.py",
        "/kolo/pytest_plugin.py",
        "/kolo/serialize.py",
        "/kolo/utils.py",
        "/kolo/version.py");
}
#[cfg(not(target_os = "windows"))]
use not_windows::*;

pub fn use_django_filter(filename: &str) -> bool {
    MIDDLEWARE_FINDER.find(filename).is_some()
}

pub fn use_django_checks_filter(filename: &str) -> bool {
    DJANGO_CHECKS_FINDER.find(filename).is_some()
}

pub fn use_django_test_db_filter(filename: &str) -> bool {
    DJANGO_TEST_DB_FINDER.find(filename).is_some()
}

pub fn use_django_setup_filter(filename: &str) -> bool {
    DJANGO_SETUP_FINDER.find(filename).is_some()
}

pub fn use_django_template_filter(filename: &str) -> bool {
    TEMPLATE_FINDER.find(filename).is_some()
}

pub fn use_celery_filter(filename: &str) -> bool {
    CELERY_FINDER.find(filename).is_some() && SENTRY_FINDER.find(filename).is_none()
}

pub fn use_huey_filter(
    filename: &str,
    huey_filter: &PyAny,
    py: Python,
    pyframe: &PyFrame,
) -> Result<bool, PyErr> {
    if HUEY_FINDER.find(filename).is_some() {
        let task_class = huey_filter.getattr(intern!(py, "klass"))?;
        if task_class.is_none() {
            let huey_api = PyModule::import(py, "huey.api")?;
            let task_class = huey_api.getattr(intern!(py, "Task"))?;
            huey_filter.setattr("klass", task_class)?;
        }

        let task_class = huey_filter.getattr(intern!(py, "klass"))?;
        let task_class = task_class.downcast()?;
        let frame_locals = pyframe.getattr(intern!(py, "f_locals"))?;
        let task = frame_locals.get_item("self")?;
        task.is_instance(task_class)
    } else {
        Ok(false)
    }
}

pub fn use_httpx_filter(filename: &str) -> bool {
    HTTPX_FINDER.find(filename).is_some()
}

pub fn use_requests_filter(filename: &str) -> bool {
    REQUESTS_FINDER.find(filename).is_some()
}

pub fn use_urllib_filter(filename: &str) -> bool {
    URLLIB_FINDER.find(filename).is_some()
}

pub fn use_urllib3_filter(filename: &str) -> bool {
    URLLIB3_FINDER.find(filename).is_some()
}

pub fn use_exception_filter(filename: &str, event: &str) -> bool {
    event == "call" && DJANGO_FINDER.find(filename).is_some()
}

pub fn use_logging_filter(filename: &str, event: &str) -> bool {
    event == "return" && LOGGING_FINDER.find(filename).is_some()
}

#[derive(Serialize)]
struct UserCodeCallSite<'a> {
    call_frame_id: &'a str,
    line_number: usize,
}

#[derive(Serialize)]
struct QueryStart<'a> {
    database: &'a str,
    frame_id: &'a str,
    user_code_call_site: Option<UserCodeCallSite<'a>>,
    call_timestamp: f64,
    thread: &'a str,
    thread_native_id: usize,
    timestamp: f64,
    #[serde(rename = "type")]
    _type: &'a str,
}

struct QueryEnd<'a> {
    database: &'a str,
    frame_id: &'a str,
    query: Option<&'a str>,
    query_data: &'a PyObject,
    query_template: Option<&'a str>,
    return_timestamp: f64,
    thread: &'a str,
    thread_native_id: usize,
    timestamp: f64,
    _type: &'a str,
}

impl QueryEnd<'_> {
    fn as_msgpack(&self, py: Python) -> Result<Vec<u8>, PyErr> {
        let mut query_data = utils::dump_msgpack(py, self.query_data.downcast::<PyAny>(py)?)?;

        let mut buf = vec![];
        rmp::encode::write_map_len(&mut buf, 10).unwrap();
        utils::write_str_pair(&mut buf, "database", Some(self.database));
        utils::write_str_pair(&mut buf, "frame_id", Some(self.frame_id));
        utils::write_str_pair(&mut buf, "query", self.query);
        utils::write_raw_pair(&mut buf, "query_data", &mut query_data);
        utils::write_str_pair(&mut buf, "query_template", self.query_template);
        utils::write_f64_pair(&mut buf, "return_timestamp", self.return_timestamp);
        utils::write_str_pair(&mut buf, "thread", Some(self.thread));
        utils::write_int_pair(&mut buf, "thread_native_id", self.thread_native_id);
        utils::write_f64_pair(&mut buf, "timestamp", self.timestamp);
        utils::write_str_pair(&mut buf, "type", Some(self._type));
        Ok(buf)
    }
}

pub struct SQLFilter {
    sql_update_compiler_code: Option<PyObject>,
    frame_ids: RefCell<HashMap<usize, String>>,
}

impl SQLFilter {
    pub fn new() -> Self {
        Self {
            sql_update_compiler_code: None,
            frame_ids: HashMap::new().into(),
        }
    }

    pub fn use_sql_filter(
        &mut self,
        filename: &str,
        py: Python,
        pyframe: &PyFrame,
    ) -> Result<bool, PyErr> {
        if SQL_FINDER.find(filename).is_some() {
            if self.sql_update_compiler_code.is_none() {
                let compiler = PyModule::import(py, "django.db.models.sql.compiler")?;
                let sql_update_compiler_code = compiler
                    .getattr(intern!(py, "SQLUpdateCompiler"))?
                    .getattr(intern!(py, "execute_sql"))?
                    .getattr(intern!(py, "__code__"))?;
                self.sql_update_compiler_code = Some(sql_update_compiler_code.extract()?);
            }
            let f_code = pyframe.getattr(intern!(py, "f_code"))?;
            Ok(!f_code.is(self.sql_update_compiler_code.as_ref().unwrap()))
        } else {
            Ok(false)
        }
    }

    pub fn process(
        &self,
        frame: &PyObject,
        event: &str,
        arg: &PyObject,
        call_frames: Vec<(PyObject, String)>,
        py: Python,
    ) -> Result<Vec<u8>, PyErr> {
        let timestamp = utils::timestamp();
        let threading = PyModule::import(py, "threading")?;
        let thread = threading.call_method0(intern!(py, "current_thread"))?;
        let locals = frame.getattr(py, intern!(py, "f_locals"))?;
        let locals = locals.downcast::<PyDict>(py)?;
        let _self = locals.get_item(intern!(py, "self"))?.unwrap();
        let connection = _self.getattr(intern!(py, "connection"))?;
        let database = connection.getattr(intern!(py, "vendor"))?;
        let database = database.extract()?;
        let pyframe_id = frame.as_ptr() as usize;

        match event {
            "call" => {
                let frame_id = utils::frame_id();
                self.frame_ids
                    .borrow_mut()
                    .insert(pyframe_id, frame_id.clone());
                let user_code_call_site = match call_frames.last() {
                    Some((call_frame, call_frame_id)) => Some(UserCodeCallSite {
                        call_frame_id,
                        line_number: call_frame
                            .getattr(py, intern!(py, "f_lineno"))?
                            .extract(py)?,
                    }),
                    None => None,
                };

                let start = QueryStart {
                    database,
                    frame_id: &frame_id,
                    user_code_call_site,
                    call_timestamp: utils::timestamp(),
                    thread: thread.getattr(intern!(py, "name"))?.extract()?,
                    thread_native_id: thread.getattr(intern!(py, "native_id"))?.extract()?,
                    timestamp,
                    _type: "start_sql_query",
                };
                Ok(rmp_serde::encode::to_vec_named(&start).unwrap())
            }
            "return" => {
                let sql = locals.get_item(intern!(py, "sql"))?;
                let params = locals.get_item(intern!(py, "params"))?;
                let (query_template, query) = match (sql, params) {
                    (Some(sql), Some(params)) => {
                        let query_template: &str = sql.extract()?;
                        if query_template.is_empty() {
                            (None, None)
                        } else {
                            let cursor = locals.get_item(intern!(py, "cursor"))?;
                            let ops = connection.getattr(intern!(py, "ops"))?;
                            let query =
                                ops.call_method1("last_executed_query", (cursor, sql, params))?;
                            (
                                Some(query_template.trim()),
                                Some(query.extract::<&str>()?.trim()),
                            )
                        }
                    }
                    _ => (None, None),
                };
                let end = QueryEnd {
                    database,
                    frame_id: &self.frame_ids.borrow()[&pyframe_id],
                    return_timestamp: utils::timestamp(),
                    query_template,
                    query,
                    query_data: arg,
                    thread: thread.getattr(intern!(py, "name"))?.extract()?,
                    thread_native_id: thread.getattr(intern!(py, "native_id"))?.extract()?,
                    timestamp,
                    _type: "end_sql_query",
                };
                end.as_msgpack(py)
            }
            _ => unreachable!(),
        }
    }
}

pub fn use_pytest_filter(filename: &str, event: &str) -> bool {
    event == "call" && PYTEST_FINDER.find(filename).is_some()
}

pub fn use_unittest_filter(filename: &str, event: &str) -> bool {
    event == "call" && UNITTEST_FINDER.find(filename).is_some()
}

pub fn library_filter(co_filename: &str) -> bool {
    for finder in LIBRARY_FINDERS.iter() {
        if finder.find(co_filename).is_some() {
            return true;
        }
    }
    #[cfg(target_os = "windows")]
    {
        (LOWER_PYTHON_FINDER.find(co_filename).is_some()
            || UPPER_PYTHON_FINDER.find(co_filename).is_some())
            && (LOWER_LIB_FINDER.find(co_filename).is_some()
                || UPPER_LIB_FINDER.find(co_filename).is_some())
    }
    #[cfg(not(target_os = "windows"))]
    false
}

pub fn frozen_filter(co_filename: &str) -> bool {
    FROZEN_FINDER.find(co_filename).is_some()
}

pub fn exec_filter(co_filename: &str) -> bool {
    EXEC_FINDER.find(co_filename).is_some()
}

pub fn kolo_filter(co_filename: &str) -> bool {
    KOLO_FINDERS
        .iter()
        .any(|finder| finder.find(co_filename).is_some())
}

pub fn attrs_filter(co_filename: &str, pyframe: &PyFrame, py: Python) -> Result<bool, PyErr> {
    if co_filename.starts_with("<attrs generated") {
        return Ok(true);
    }

    let previous = pyframe.getattr(intern!(py, "f_back"))?;
    if previous.is_none() {
        return Ok(false);
    }

    let f_code = previous.getattr(intern!(py, "f_code"))?;
    let co_filename = f_code.getattr(intern!(py, "co_filename"))?;
    let co_filename = co_filename.extract::<String>()?;

    #[cfg(target_os = "windows")]
    let make_path = "attr\\_make.py";
    #[cfg(not(target_os = "windows"))]
    let make_path = "attr/_make.py";

    if co_filename.is_empty() {
        let previous = previous.getattr(intern!(py, "f_back"))?;
        if previous.is_none() {
            return Ok(false);
        }
        let f_code = previous.getattr(intern!(py, "f_code"))?;
        let co_filename = f_code.getattr(intern!(py, "co_filename"))?;
        let co_filename = co_filename.extract::<String>()?;
        Ok(co_filename.ends_with(make_path))
    } else {
        Ok(co_filename.ends_with(make_path))
    }
}
