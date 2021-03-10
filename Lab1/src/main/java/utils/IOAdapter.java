package utils;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class IOAdapter {
    private BufferedWriter writer;
    private BufferedReader reader;

    public IOAdapter(InputStream in, OutputStream out) {
        writer = new BufferedWriter(new OutputStreamWriter(out));
        reader = new BufferedReader(new InputStreamReader(in));
    }

    public void write(String str) throws IOException {
        writer.write(str);
        writer.flush();
    }

    public void writeln(String str) throws IOException {
        write(str + "\n");
    }

    public String readLine() throws IOException {
        return reader.readLine().trim();
    }

    public Integer readInt(int min, int max, String message) throws Exception {
        int n;
        while (true) {
            try {
                writeln(message);
                n = Integer.parseInt(readLine());
                if (n < min) {
                    writeln("Вводимое значение не может быть меньше, чем " + min);
                } else if (n > max) {
                    writeln("Вводимое значение не может быть больше, чем " + max);
                } else break;
            } catch (NumberFormatException e) {
                writeln("Ошибка вводимого значения, оно не явлется Целым числом");
            }
        }
        return n;
    }

    public <T extends Enum<T>> T chooseEnum(Class<T> aEnum) throws Exception {
        List<T> enums = java.util.Arrays.asList(aEnum.getEnumConstants());
        for (int i = 0; i < enums.size(); i++) {
            writeln(i + ": " + enums.get(i));
        }
        int selectedEnum = readInt(0, enums.size()-1, "Выберите номер ");
        return enums.get(selectedEnum);
    }

    public InputStream getISFromFile() throws IOException {
        while (true) {
            try {
                writeln("Введите название файла");
                return new FileInputStream(new File(readLine()));
            } catch (Exception e) {
                List<File> files = new ArrayList<>();
                writeln("Не удалось найти файл, ознакомьтесь со структурой директории");
                doListing( new File(new File(".").getAbsolutePath()+"/src"), files);
                files.forEach(System.out::println);
            }
        }
    }

    private List<File> doListing(File dirName, List<File> files) {

        File[] fileList = dirName.listFiles();

        for (File file : fileList) {

            if (file.isFile()) {

                files.add(file);
            } else if (file.isDirectory()) {

                files.add(file);
                doListing(file, files);
            }
        }

        return files;
    }

    public void setWriter(BufferedWriter writer) {
        this.writer = writer;
    }

    public void setReader(BufferedReader reader) {
        this.reader = reader;
    }

    public BufferedReader getReader() {
        return reader;
    }

    public BufferedWriter getWriter() {
        return writer;
    }
}
