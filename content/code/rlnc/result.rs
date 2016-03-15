use std::collections::VecDeque;

fn main() {
    let mut queue: VecDeque<u64> = VecDeque::new();

    queue.push_front(42u64);
    queue.push_front(69u64);

    loop {
        match queue.pop_back() {
            Some(element) => println!("Il reste un élément : {}", element),
            None => break,
        }
    }
}
