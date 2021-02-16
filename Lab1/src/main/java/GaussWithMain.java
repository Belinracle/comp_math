import utils.IOAdapter;

public class GaussWithMain {
    public static void main(String[] args) throws Exception {
        EquationSystemShell shell = new EquationSystemShell(new IOAdapter(System.in, System.out));
        shell.prepare("commands");
        while (true) {
            shell.work();
        }
    }

}
