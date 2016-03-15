public interface Bonjour {
    public void dire_bonjour();
}

public class Personne implements Bonjour {
    public String name;

    public void dire_bonjour() {
        System.out.println("Bonjour, je m'appelle " + this.name);
    }

    public Personne(String name) {
        this.name = name;
    }
}

public class equivalent {
    public static void main(String[] args) {
        Personne p = new Personne("John Smith");
        p.dire_bonjour();
    }
}
