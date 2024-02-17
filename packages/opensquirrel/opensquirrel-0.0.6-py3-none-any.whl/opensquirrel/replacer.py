from typing import Callable, List

from opensquirrel.circuit_matrix_calculator import get_circuit_matrix
from opensquirrel.common import are_matrices_equivalent_up_to_global_phase
from opensquirrel.squirrel_ir import (
    BlochSphereRotation,
    ControlledGate,
    Gate,
    MatrixGate,
    Qubit,
    SquirrelIR,
    SquirrelIRVisitor,
)


class _QubitRemapper(SquirrelIRVisitor):
    def __init__(self, mappings: List[Qubit]):
        self.mappings = mappings

    def visit_bloch_sphere_rotation(self, g: BlochSphereRotation):
        result = BlochSphereRotation(
            qubit=Qubit(self.mappings.index(g.qubit)), angle=g.angle, axis=g.axis, phase=g.phase
        )
        return result

    def visit_matrix_gate(self, g: MatrixGate):
        mapped_operands = [Qubit(self.mappings.index(op)) for op in g.operands]
        result = MatrixGate(matrix=g.matrix, operands=mapped_operands)
        return result

    def visit_controlled_gate(self, controlled_gate: ControlledGate):
        control_qubit = Qubit(self.mappings.index(controlled_gate.control_qubit))
        target_gate = controlled_gate.target_gate.accept(self)
        result = ControlledGate(control_qubit=control_qubit, target_gate=target_gate)
        return result


def get_replacement_matrix(replacement: List[Gate], qubit_mappings):
    replacement_ir = SquirrelIR(number_of_qubits=len(qubit_mappings), qubit_register_name="whatever")
    qubit_remapper = _QubitRemapper(qubit_mappings)

    for gate in replacement:
        gate_with_remapped_qubits = gate.accept(qubit_remapper)
        replacement_ir.add_gate(gate_with_remapped_qubits)

    return get_circuit_matrix(replacement_ir)


def check_valid_replacement(statement, replacement):
    expected_qubit_operands = statement.get_qubit_operands()
    replacement_qubit_operands = set()
    [replacement_qubit_operands.update(g.get_qubit_operands()) for g in replacement]

    if set(expected_qubit_operands) != replacement_qubit_operands:
        raise Exception(f"Replacement for gate {statement.name} does not seem to operate on the right qubits")

    replacement_matrix = get_replacement_matrix(replacement, expected_qubit_operands)
    replaced_matrix = get_replacement_matrix([statement], expected_qubit_operands)

    if not are_matrices_equivalent_up_to_global_phase(replacement_matrix, replaced_matrix):
        raise Exception(f"Replacement for gate {statement.name} does not preserve the quantum state")


def decompose(squirrel_ir: SquirrelIR, decomposer: Callable[[Gate], List[Gate]]):
    """Applies `decomposer` to every gate in the circuit, replacing each gate by the output of `decomposer`.
    When `decomposer` decides to not decompose a gate, it needs to return a list with the intact gate as single element.
    """
    statement_index = 0
    while statement_index < len(squirrel_ir.statements):
        statement = squirrel_ir.statements[statement_index]

        if not isinstance(statement, Gate):
            statement_index += 1
            continue

        replacement: List[Gate] = decomposer(statement)

        check_valid_replacement(statement, replacement)

        squirrel_ir.statements[statement_index : statement_index + 1] = replacement
        statement_index += len(replacement)


def replace(squirrel_ir: SquirrelIR, gate_generator: Callable[..., Gate], f):
    """Does the same as decomposer, but only applies to a given gate."""

    def generic_replacer(g: Gate) -> [Gate]:
        if g.is_anonymous or g.generator != gate_generator:
            return [g]
        return f(*g.arguments)

    decompose(squirrel_ir, generic_replacer)
