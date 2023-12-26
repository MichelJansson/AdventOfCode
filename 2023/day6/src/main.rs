use std::fs;

fn main() {
    let input = fs::read_to_string("input.txt").expect("Could not read input.txt");
    let mut part1_times: Vec<i32> = Vec::new();
    let mut part1_distances: Vec<i32> = Vec::new();

    for line in input.lines() {
        let parts: Vec<&str> = line.split(':').collect();
        if part1_times.is_empty() {
            part1_times = parts[1]
                .split_whitespace()
                .map(|x| x.parse::<i32>().unwrap())
                .collect();
        } else {
            part1_distances = parts[1]
                .split_whitespace()
                .map(|x| x.parse::<i32>().unwrap())
                .collect();
        }
    }

    let mut part1_result = 0;

    for (record_time, record_distance) in part1_times.iter().zip(part1_distances) {
        let mut better_ways = 0;

        for time in 0..*record_time {
            let distance = time * (record_time - time);

            if distance > record_distance {
                better_ways += 1;
            }
        }

        if part1_result == 0 {
            part1_result = better_ways;
        } else {
            part1_result *= better_ways;
        }
    }

    println!("Part 1 result: {part1_result}");

    let mut part2_time: i64 = 0;
    let mut part2_distance: i64 = 0;

    for line in input.lines() {
        let parts: Vec<&str> = line.split(':').collect();
        if part2_time == 0 {
            part2_time = parts[1].replace(" ", "").parse::<i64>().unwrap();
        } else {
            part2_distance = parts[1].replace(" ", "").parse::<i64>().unwrap();
        }
    }

    let mut part2_result = 0;

    for time in 0..part2_time {
        let distance = time * (part2_time - time);

        if distance > part2_distance {
            part2_result += 1;
        }
    }

    println!("Part 2 result: {part2_result}");
}
