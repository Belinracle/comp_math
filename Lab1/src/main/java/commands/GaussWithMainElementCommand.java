package commands;

import equationSystem.EquationSystem;
import equationSystem.Matrix;
import equationSystem.MatrixRow;
import utils.IOAdapter;

import javax.jws.soap.SOAPBinding;
import java.io.IOException;
import java.util.LinkedList;
import java.util.List;

public class GaussWithMainElementCommand implements Command {
    private final String name;
    private final String description;

    enum Solution{
        ONE_SOLUTION,
        INFINITY_SOLUTION,
        NO_SOLUTION
    }

    public GaussWithMainElementCommand() {
        name = "gauss_main_elem";
        description = "решение системы методом гаусса с выбором главного элемента";
    }

    @Override
    public void perform(EquationSystem system, IOAdapter adapter) throws IOException {
        if (system.getMatrix() == null) {
            adapter.writeln("Система не создана");
            return;
        }
        Matrix triangleMatrix = system.getMatrix().copy();
        int n = triangleMatrix.size() - 1;
        LinkedList<MatrixRow> a = triangleMatrix.getMatrixRows();

        for (int i = 0; i <= n - 1; i++) {
            //выбор главного элемента
            int l = i;
            for (int m = i + 1; m <= n; m++) {
                if (a.get(m).getByIndex(i) > a.get(l).getByIndex(i)) {
                    l = m;
                }
            }
            if (l != i) {
                triangleMatrix.swapRows(i, l);
            }
            //конец перестановки с выбором главного элемента
            for (int k = i + 1; k <= n; k++) {
                double c = a.get(k).getByIndex(i) / a.get(i).getByIndex(i);
                MatrixRow buffer = a.get(i).copy();
                buffer.multiply(c);
                buffer.setByIndex(i, 0D);
                a.get(k).setByIndex(i, 0D);
                a.get(k).subtract(buffer);
            }
        }
        Solution solution = checkSolution(triangleMatrix);
        switch (solution){
            case ONE_SOLUTION:
                Double[] gaussSolutions = new Double[n + 1];
                for (int i = n; i >= 0; i--) {
                    double s = 0;
                    for (int j = i + 1; j <= n; j++) {
                        s = s + a.get(i).getByIndex(j) * gaussSolutions[j];
                    }
                    gaussSolutions[i] = (a.get(i).getByIndex(n + 1) - s) / a.get(i).getByIndex(i);
                }
                system.setSolutions(gaussSolutions);
                break;
            case INFINITY_SOLUTION:
                adapter.writeln("Система имеет бесконечное число решений");
                break;
            case NO_SOLUTION:
                adapter.writeln("Система не имеет решений");
                break;
        }
        system.addView(name, triangleMatrix);
    }

    private Solution checkSolution(Matrix triangleMatrix){
        int extRang = calcExtMtxRang(triangleMatrix);
        int rang = calcMtxRang(triangleMatrix);
        if (extRang!=rang) return Solution.NO_SOLUTION;
        else if( rang != triangleMatrix.size()){
            return Solution.INFINITY_SOLUTION;
        }
        else return Solution.ONE_SOLUTION;
    }

    private int calcMtxRang(Matrix matrix) {
        int rang = 0;
        for (MatrixRow row : matrix.getMatrixRows()) {
            List<Double> coeffs = row.getQuotients();
            boolean isFullZero = true;
            for (int counter = 0; counter < row.getQuotients().size() - 1; counter++) {
                if (coeffs.get(counter)!=0) isFullZero = false;
            }
            if(!isFullZero)rang++;
        }
        return rang;
    }

    private int calcExtMtxRang(Matrix matrix) {
        int extRang = 0;
        for (MatrixRow row:matrix.getMatrixRows()){
            if(row.getQuotients().stream().anyMatch((elem) -> elem != 0))extRang++;
        }
        return extRang;
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
