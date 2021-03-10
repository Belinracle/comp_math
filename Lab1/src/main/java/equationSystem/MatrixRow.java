package equationSystem;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

import static java.util.stream.Collectors.toList;

public class MatrixRow {
    private List<Double> quotients;

    public MatrixRow(List<Double> quotients) {
        this.quotients = quotients;
    }

    public void multiply(double factor) {
        quotients = quotients.stream().map((elem) -> elem!=0?elem*factor:elem ).collect(toList());
    }

    public void subtract(MatrixRow subtractedRow){
        for(int counter = 0; counter<quotients.size();counter++){
            quotients.set(counter,quotients.get(counter) - subtractedRow.getQuotients().get(counter));
        }
    }

    public Double getByIndex(int index){
        return quotients.get(index);
    }

    public Double setByIndex(int index, Double value){
        return quotients.set(index,value);
    }
    public MatrixRow copy(){
        List<Double> quotientsCopy = quotients.stream().map(Double::new).collect(toList());
        return new MatrixRow(quotientsCopy);
    }

    public List<Double> getQuotients() { return quotients; }
    public void setQuotients(List<Double> quotients) { this.quotients = quotients; }
}
