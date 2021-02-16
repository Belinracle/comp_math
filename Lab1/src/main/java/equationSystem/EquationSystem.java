package equationSystem;

import java.util.HashMap;
import java.util.List;

public class EquationSystem {
    private Matrix matrix;
    private Double determinant;
    private HashMap<String,Matrix> differentViews;
    private Double[] solutions;
    private List<Double> inaccuracy;


    public void addView( String view, Matrix matrix){
        differentViews.put(view,matrix);
    }

    public void reset(){
        matrix=null;
        determinant=null;
        differentViews=new HashMap<>();
        solutions=null;
        inaccuracy=null;
    }

    public Matrix getMatrix() { return matrix; }
    public void setMatrix(Matrix matrix) { this.matrix = matrix; }
    public Double getDeterminant() { return determinant; }
    public void setDeterminant(Double determinant) { this.determinant = determinant; }
    public HashMap<String, Matrix> getDifferentViews() { return differentViews; }
    public void setDifferentViews(HashMap<String, Matrix> differentViews) { this.differentViews = differentViews;}
    public Double[] getSolutions() { return solutions; }
    public void setSolutions(Double[] solutions) { this.solutions = solutions; }
    public List<Double> getInaccuracy() { return inaccuracy; }
    public void setInaccuracy(List<Double> inaccuracy) { this.inaccuracy = inaccuracy; }
}
