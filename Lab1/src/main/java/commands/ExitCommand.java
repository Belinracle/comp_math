package commands;

import equationSystem.EquationSystem;
import utils.IOAdapter;

public class ExitCommand implements Command{

    private final String name;
    private final String description;

    public ExitCommand(){
        name="exit";
        description="завершить выполнение программы";
    }

    @Override
    public void perform(EquationSystem system, IOAdapter talkToClient) throws Exception {
        System.exit(0);
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
