from .utils.log_config import setup_logging

from .dataset.tabledata.titanic.preprocessing import titanic_data
from .metrix.binary_classification import binary_classification, binary_classification_objective

from .train.optuna import exec_optuna
from .utils.log_config import setup_logging

result_logger, _ = setup_logging()


class AutoResEvaluator():
    def __init__(
            self,
            task_type,
            dataset_name,
            model_path,
            params,
            valuation_index
            ) -> None:
        self.task_type = task_type
        self.dataset_name = dataset_name
        self.model_path = model_path
        self.params = params
        self.valuation_index = valuation_index
        self.objective = binary_classification_objective(self.valuation_index)
        self._select_dataset()
        pass

    def _select_dataset(self):
        if self.task_type == 'tabledata binary classification':
            if self.dataset_name == 'titanic':
                self.dataset = titanic_data()
                self.metrix = binary_classification
            pass
        elif self.task_type == 'tabledata regression':
            pass
        elif self.task_type == 'image classification':
            pass
        elif self.task_type == 'text classification':
            pass

    def exec(self):
        #os.makedirs(directory, exist_ok=True)
        result_logger.info('------auto evaluate start------')
        result_logger.info(f'task type: {self.task_type}')
        result_logger.info(f'dataset name: {self.dataset_name}')
        result_logger.info(f'model path: {self.model_path}')
        result_logger.info(f'valuation_index: {self.valuation_index}')
        result_logger.info(f'objective: {self.objective}')
        exec_optuna(self.model_path, self.dataset, self.metrix, self.params, self.valuation_index, self.objective)
        pass
