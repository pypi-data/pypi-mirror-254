from dataclasses import dataclass

from qtpy.QtWidgets import QFormLayout, QLabel, QSpinBox

from ert.gui.ertnotifier import ErtNotifier
from ert.gui.ertwidgets import AnalysisModuleEdit, CaseSelector
from ert.gui.ertwidgets.copyablelabel import CopyableLabel
from ert.gui.ertwidgets.models.activerealizationsmodel import ActiveRealizationsModel
from ert.gui.ertwidgets.models.targetcasemodel import TargetCaseModel
from ert.gui.ertwidgets.stringbox import StringBox
from ert.libres_facade import LibresFacade
from ert.run_models import IteratedEnsembleSmoother
from ert.validation import ProperNameFormatArgument, RangeStringArgument

from .simulation_config_panel import SimulationConfigPanel


@dataclass
class Arguments:
    mode: str
    current_case: str
    target_case: str
    realizations: str
    num_iterations: int


class IteratedEnsembleSmootherPanel(SimulationConfigPanel):
    def __init__(self, facade: LibresFacade, notifier: ErtNotifier, ensemble_size: int):
        self.facade = facade
        self.notifier = notifier
        SimulationConfigPanel.__init__(self, IteratedEnsembleSmoother)

        layout = QFormLayout()

        case_selector = CaseSelector(notifier)
        layout.addRow("Current case:", case_selector)

        runpath_label = CopyableLabel(text=self.facade.run_path_stripped)
        layout.addRow("Runpath:", runpath_label)

        number_of_realizations_label = QLabel(f"<b>{ensemble_size}</b>")
        layout.addRow(QLabel("Number of realizations:"), number_of_realizations_label)

        # The num_iterations_spinner does not track any external changes (will
        # that ever happen?)
        self._num_iterations_spinner = QSpinBox()
        self._num_iterations_spinner.setMinimum(1)
        self._num_iterations_spinner.setMaximum(100)
        self._num_iterations_spinner.setValue(self.facade.get_number_of_iterations())
        self._num_iterations_spinner.valueChanged[int].connect(self.setNumberIterations)

        layout.addRow("Number of iterations:", self._num_iterations_spinner)

        self._iterated_target_case_format_model = TargetCaseModel(
            self.facade, notifier, format_mode=True
        )
        self._iterated_target_case_format_field = StringBox(
            self._iterated_target_case_format_model,
            "config/simulation/iterated_target_case_format",
        )
        self._iterated_target_case_format_field.setValidator(ProperNameFormatArgument())
        layout.addRow("Target case format:", self._iterated_target_case_format_field)

        self._analysis_module_edit = AnalysisModuleEdit(
            self.facade.get_analysis_module("IES_ENKF"), ensemble_size
        )
        layout.addRow("Analysis module:", self._analysis_module_edit)

        self._active_realizations_model = ActiveRealizationsModel(ensemble_size)
        self._active_realizations_field = StringBox(
            self._active_realizations_model, "config/simulation/active_realizations"
        )
        self._active_realizations_field.setValidator(RangeStringArgument(ensemble_size))
        layout.addRow("Active realizations", self._active_realizations_field)

        self._iterated_target_case_format_field.getValidationSupport().validationChanged.connect(  # noqa
            self.simulationConfigurationChanged
        )
        self._active_realizations_field.getValidationSupport().validationChanged.connect(  # noqa
            self.simulationConfigurationChanged
        )

        self.setLayout(layout)

    def setNumberIterations(self, iteration_count):
        if iteration_count != self.facade.get_number_of_iterations():
            self.facade.get_analysis_config().set_num_iterations(iteration_count)
            self.notifier.emitErtChange()

    def isConfigurationValid(self):
        return (
            self._iterated_target_case_format_field.isValid()
            and self._active_realizations_field.isValid()
        )

    def getSimulationArguments(self):
        return Arguments(
            mode="iterative_ensemble_smoother",
            current_case=self.notifier.current_case_name,
            target_case=self._iterated_target_case_format_model.getValue(),
            realizations=self._active_realizations_field.text(),
            num_iterations=self._num_iterations_spinner.value(),
        )
