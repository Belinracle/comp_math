package commands;

import equationSystem.EquationSystem;
import equationSystem.MatrixRow;
import utils.IOAdapter;

import java.io.IOException;
import java.util.LinkedList;

public class DeterminantCalculatorTriangleMatrixCommand implements Command{
    private final String name;
    private final String description;

    public DeterminantCalculatorTriangleMatrixCommand() {
        name = "calculate_determinant_triangle";
        description = "посчитать детерминант треугольной матрицы";
    }

    @Override
    public void perform(EquationSystem system, IOAdapter adapter) throws IOException {
        if(system.getMatrix() == null){
            adapter.writeln("Система не создана");
            return;
        }
        if(system.getDifferentViews().get("gauss_main_elem")==null){
            adapter.writeln("Для начала необходимо вызвать команду gauss_main_elem");
            return;
        }
        double result = 1;
        LinkedList<MatrixRow> list = system.getMatrix().getMatrixRows();
        for (int counter = 0; counter < list.size(); counter++) {
            result = result * list.get(counter).getByIndex(counter);
        }
        system.setDeterminant(result);
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public String getDescription() {
        return description;
    }
}
