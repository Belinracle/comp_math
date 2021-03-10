import commands.Command;
import equationSystem.EquationSystem;
import org.reflections.Reflections;
import utils.IOAdapter;

import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.util.Collection;
import java.util.HashMap;
import java.util.Set;

public class EquationSystemShell {
    private final HashMap<String, Command> commandsByNames;
    private final HashMap<String, String> commandsDescription;
    private EquationSystem system;
    private final IOAdapter adapter;

    public EquationSystemShell(IOAdapter adapter) {
        this.adapter = adapter;
        commandsByNames = new HashMap<>();
        commandsDescription = new HashMap<>();
        system = new EquationSystem();
    }

    public void work(){
        try {
            adapter.writeln("Введите команду");
            commandsDescription.forEach((command, description)-> {
                try {
                    adapter.writeln(command +"->"+description);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            });
            String command = adapter.readLine();
            try {
                commandsByNames.get(command).perform(system,adapter);
            }catch (NullPointerException e){
                adapter.writeln("Такой команды не существует");
            }
        }catch(Exception e){
            e.printStackTrace();
        }
    }

    public void prepare(String packageToScan) throws Exception{
        Reflections scanner = new Reflections(packageToScan);
        Set<Class<? extends Command>> classes = scanner.getSubTypesOf(Command.class);
        for (Class<? extends Command> commandClass : classes) {
            Command command = commandClass.getDeclaredConstructor().newInstance();
            commandsByNames.put(command.getName(), command);
        }
        makeCommandsInfo();
    }

    private void makeCommandsInfo() {
        Collection<Command> commands = commandsByNames.values();
        for (Command command : commands) {
            commandsDescription.put(command.getName(), command.getDescription());
        }
    }
}
