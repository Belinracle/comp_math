package commands;

import equationSystem.EquationSystem;
import equationSystem.Matrix;
import equationSystem.MatrixRow;
import utils.IOAdapter;

import java.io.IOException;
import java.util.*;
import java.util.stream.Collectors;

public class CreateEquationSystemCommand implements Command {
    private final String name;
    private final String description;

    private enum TypeOfCreating {
        FROM_FILE,
        FROM_CONSOLE,
        RANDOM_VALUES
    }

    public CreateEquationSystemCommand() {
        name = "create_system";
        description = "создать систему уравнений";
    }

    @Override
    public void perform(EquationSystem system, IOAdapter adapter) throws Exception {
        system.reset();
        TypeOfCreating type = adapter.chooseEnum(TypeOfCreating.class);
        switch (type) {
            case FROM_FILE:
                system.setMatrix(readSystem(new IOAdapter(adapter.getISFromFile(), System.out)));
                break;
            case FROM_CONSOLE:
                system.setMatrix(readSystem(adapter));
                break;
            case RANDOM_VALUES:
                system.setMatrix(createRandomMatrix(adapter));
                break;
        }
    }

    private Matrix createRandomMatrix(IOAdapter adapter) throws Exception {
        int n = adapter.readInt(1, Integer.MAX_VALUE, "Введите n");
        LinkedList<MatrixRow> rows = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            List<Double> doubles = new ArrayList<>();
            for (int j = 0; j < n + 1; j++) {
                doubles.add(createRandomDouble(500D,-500D));
            }
            rows.add(new MatrixRow(doubles));
        }
        return new Matrix(rows);
    }

    private Double createRandomDouble(Double min,Double max){
        int result=0;
        while(result==0) {
            result = (int) (min + (Math.random() * (max - min)));
        }
        return (double) result;
    }

    public Matrix readSystem(IOAdapter adapter) throws IOException {
        try {
            int n = adapter.readInt(1, Integer.MAX_VALUE, "Введите n");
            adapter.writeln("Введите коэффициенты уравнений и b");
            LinkedList<MatrixRow> matrixRows = new LinkedList<MatrixRow>();
            for (int i = 1; i <= n; i++) {
                while (true) {
                    adapter.writeln("Введите строку " + i);
                    List<Double> coefficientsInRowAsDoubles = new ArrayList();
                    List<String> coefficientsInRowAsStrings = Arrays.stream(adapter.readLine().split(" ")).map(String::trim).collect(Collectors.toList());
                    try {
                        coefficientsInRowAsDoubles = coefficientsInRowAsStrings.stream().map(Double::parseDouble).collect(Collectors.toList());
                    } catch (NumberFormatException e) {
                        adapter.writeln("Введенные коэффициенты не соответствую типу Double");
                    }
                    if (coefficientsInRowAsDoubles.size() != n + 1) {
                        adapter.writeln("Не забудьте ввести b, и не вводите лишних коэффициентов");
                    } else {
                        matrixRows.addLast(new MatrixRow(coefficientsInRowAsDoubles));
                        break;
                    }
                }
            }
            return new Matrix(matrixRows);
        } catch (Exception e) {
            adapter.writeln("Проблема потока ввода, операция не может быть завершена");
        }
        return null;
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
