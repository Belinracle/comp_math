package commands;

import equationSystem.EquationSystem;
import equationSystem.Matrix;
import equationSystem.MatrixRow;
import utils.IOAdapter;

import java.util.ArrayList;
import java.util.List;

public class CalculateInaccuracyCommand implements Command {

    private final String name;
    private final String description;

    public CalculateInaccuracyCommand() {
        name = "calculate_inaccuracy";
        description = "посчитать невязки";
    }

    @Override
    public void perform(EquationSystem system, IOAdapter adapter) throws Exception {
        if (system.getSolutions() == null) {
            adapter.writeln("Невозможно посчитать невязки, если не просчитаны решения системы");
            return;
        }
        List<Double> inaccuracy = calculateInaccuracy(system.getMatrix(),system.getSolutions());
        system.setInaccuracy(inaccuracy);
    }

    private List<Double> calculateInaccuracy(Matrix matrix, Double[] solutions) {
        List<Double> inaccuracy = new ArrayList<>();
        for (MatrixRow row : matrix.getMatrixRows()) {
            List<Double> coefficients = row.getQuotients();
            Double sum = 0D;
            for (int counter = 0; counter < coefficients.size() - 1; counter++) {
                sum = sum + coefficients.get(counter) * solutions[counter];
            }
            inaccuracy.add(coefficients.get(coefficients.size()-1)-sum);
        }
        return inaccuracy;
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
