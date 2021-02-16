package commands;

import equationSystem.EquationSystem;
import equationSystem.Matrix;
import utils.IOAdapter;

public interface Command {
    public void perform(EquationSystem system, IOAdapter talkToClient) throws Exception;
    public String getName();
    public String getDescription();
}
