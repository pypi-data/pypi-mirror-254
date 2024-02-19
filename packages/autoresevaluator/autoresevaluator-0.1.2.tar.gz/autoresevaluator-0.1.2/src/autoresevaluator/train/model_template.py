import importlib.util
import sys
import numpy as np

from ..utils.log_config import setup_logging

_, model_logger = setup_logging()

def model_template(path, X_train, y_train, X_test, params):
    try:
        model = load_method_from_path(path)
        y_pred = model(X_train, y_train, X_test, params)
        if not isinstance(y_pred, np.ndarray):
            raise model_logger.error("y_pred must be a NumPy array.")
        if y_pred.ndim != 1:
            raise model_logger.error("y_pred must be a one-dimensional array.")
        return y_pred
    except Exception as e:
        model_logger.error(f'error: {e}')

        pass


def load_method_from_path(path, method_name = 'model'):
    module_name = path.split('/')[-1].split('.')[0]

    try:
        spec = importlib.util.spec_from_file_location(module_name, path)
        model_logger.info(f'ModuleSpec: {spec}')
        module = importlib.util.module_from_spec(spec)
        model_logger.info(f'Module: {module}')
        sys.modules[module_name] = module
        spec.loader.exec_module(module)

        method = getattr(module, method_name, None)
        if method is None:
            raise model_logger.error(f"Method {method_name} not found in {path}")
        model_logger.info('メソッドが正常にインポートされました')

    except Exception as e:
        model_logger.error(f"Error importing method {method_name} from {path}: {e}")
        raise

    return method
