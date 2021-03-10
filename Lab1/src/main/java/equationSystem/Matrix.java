package equationSystem;

import java.util.*;

public class Matrix {
    private LinkedList<MatrixRow> matrixRows;

    public Matrix(LinkedList<MatrixRow> matrixRows){
        this.matrixRows=matrixRows;
    }

    public void swapRows(int firstToSwap, int secondToSwap){
        MatrixRow buffer = matrixRows.get(firstToSwap).copy();
        matrixRows.set(firstToSwap,matrixRows.get(secondToSwap));
        matrixRows.set(secondToSwap,buffer);
    }


    public Matrix copy(){
        LinkedList<MatrixRow> rowsCopy = new LinkedList<>();
        for(MatrixRow row: matrixRows){
            rowsCopy.add(row.copy());
        }
        return new Matrix(rowsCopy);
    }
    public int size(){return matrixRows.size();}

    public LinkedList<MatrixRow> getMatrixRows() {
        return matrixRows;
    }
    public void setMatrixRows(LinkedList<MatrixRow> matrixRows) {
        this.matrixRows = matrixRows;
    }
}
