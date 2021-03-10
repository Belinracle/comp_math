package commands;

import equationSystem.EquationSystem;
import equationSystem.Matrix;
import equationSystem.MatrixRow;
import utils.IOAdapter;

import java.io.IOException;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class ShowAllCommand implements Command {
    private final String name;
    private final String description;

    public ShowAllCommand() {
        name = "show";
        description = "показать информацию о текущей матрице";
    }

    @Override
    public void perform(EquationSystem system, IOAdapter adapter) throws Exception {
        if (system.getMatrix() == null) {
            adapter.writeln("Система не создана");
            return;
        }
        Matrix matrix = system.getMatrix();
        showMatrix(matrix, adapter);
        Set<Map.Entry<String, Matrix>> views = system.getDifferentViews().entrySet();
        for (Map.Entry<String, Matrix> view : views) {
            adapter.writeln(view.getKey());
            showMatrix(view.getValue(), adapter);
        }
        adapter.writeln("Детерминант системы равен: " + (system.getDeterminant()!=null?String.format("%17e", system.getDeterminant()):"еще не был вычислен"));
        showSolutions(system.getSolutions(),adapter);
        showInaccuracy(system.getInaccuracy(),adapter);
    }


    private void showMatrix(Matrix matrix, IOAdapter adapter) throws IOException {
        List<MatrixRow> rows = matrix.getMatrixRows();
        for (MatrixRow row : rows) {
            List<Double> doubles = row.getQuotients();
            for (int counter = 0; counter < doubles.size(); counter++) {
                if (counter == doubles.size() - 1) {
                    adapter.write(" || ");
                }
                adapter.write(String.format("%17.5f", doubles.get(counter)));
            }
            adapter.write("\n");
        }
    }

    private void showSolutions(Double[] solutions, IOAdapter adapter) throws IOException {
        if (solutions == null) {
            adapter.writeln("Решения не были вычислены");
        } else {
            for (int counter = 0; counter <= solutions.length-1; counter++) {
                adapter.writeln(String.format("%s%d = %17e","X",counter+1, solutions[counter]));
            }
        }
    }

    private void showInaccuracy(List<Double> inaccuracy, IOAdapter adapter) throws IOException {
        if (inaccuracy == null) {
            adapter.writeln("Невязки не были вычислены");
        } else {
            for (int counter = 0; counter <= inaccuracy.size()-1; counter++) {
                adapter.writeln(String.format("%s%d = %17e","Невязка для строки ",counter+1, inaccuracy.get(counter)));
            }
        }
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
