use fancy_regex::Regex;
use std::fs;

fn main() {
    part1();
    part2();
    part2_noregex();
}

fn part1() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to open file");
    let mut result: i32 = 0;

    let re = Regex::new(r"(?m)(?=(\d)).*(\d)\D*$").unwrap();
    for capture in re.captures_iter(&input).map(|c| c.unwrap()) {
        let first = capture.get(1).unwrap().as_str();
        let mut last = capture.get(2).unwrap().as_str();

        if last == "" {
            last = first;
        }

        let string = first.to_owned() + last;
        result += string.parse::<i32>().unwrap();
    }

    println!("Part 1: {}", result);
}

fn part2() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to open file");
    let mut result: i32 = 0;

    let re = Regex::new(r"(?m)(?=(\d|one|two|three|four|five|six|seven|eight|nine)).*(\d|one|two|three|four|five|six|seven|eight|nine).*$").unwrap();
    for capture in re.captures_iter(&input).map(|c| c.unwrap()) {
        let first = numstring_to_num(capture.get(1).unwrap().as_str());
        let mut last = numstring_to_num(capture.get(2).unwrap().as_str());

        if last == "" {
            last = first;
        }

        let string = first.to_owned() + last;
        result += string.parse::<i32>().unwrap();
    }

    println!("Part 2: {}", result);
}

fn part2_noregex() {
    let mut result: i32 = 0;

    for line in fs::read_to_string("input.txt").unwrap().lines() {
        let mut first_idx = Vec::new();
        let mut last_idx = Vec::new();

        for num in [
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five",
            "six", "seven", "eight", "nine",
        ] {
            let l = line.find(num);
            let r = line.rfind(num);
            if l > None {
                first_idx.push((l, num));
            }

            if r > None {
                last_idx.push((r, num));
            }
        }

        let (_, first) = first_idx.iter().min().unwrap();
        let (_, last) = last_idx.iter().max().unwrap();

        let string = numstring_to_num(first).to_owned() + numstring_to_num(last);

        result += string.parse::<i32>().unwrap();
    }

    println!("Part 2 (no regex): {}", result);
}

fn numstring_to_num(str: &str) -> &str {
    match str {
        "one" => return "1",
        "two" => return "2",
        "three" => return "3",
        "four" => return "4",
        "five" => return "5",
        "six" => return "6",
        "seven" => return "7",
        "eight" => return "8",
        "nine" => return "9",
        _ => return str,
    }
}
