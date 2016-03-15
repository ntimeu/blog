struct Personne {
    name: String,
}

trait Bonjour {
    fn dire_bonjour(&self);
}

impl Bonjour for Personne {
    fn dire_bonjour(&self) {
        println!("Bonjour, je m'appelle {}", self.name);
    }
}

fn main() {
    let p: Personne = Personne {
        name: String::from("John Smith"),
    };

    p.dire_bonjour();
}
