use std::{collections::HashMap, fs};

fn main() {
    let input = fs::read_to_string("input.txt").expect("Could not read input.txt");
    let mut part1_points: i32 = 0;
    let mut scratches: HashMap<usize, u32> = HashMap::new();

    for (i, line) in input.lines().enumerate() {
        scratches.entry(i).and_modify(|x| *x += 1).or_insert(1);

        let parts: Vec<&str> = line.split(&[':', '|'][..]).collect();
        let winning: Vec<&str> = parts[1].split_whitespace().collect();
        let scratch: Vec<&str> = parts[2].split_whitespace().collect();

        let won_count = scratch.iter().filter(|x| winning.contains(x)).count() as u32;

        if won_count > 0 {
            part1_points += 1_i32 * 2_i32.pow(won_count - 1);

            let scratch_count = scratches.get(&i).unwrap().to_owned();

            for j in 1..won_count + 1 {
                scratches
                    .entry(i + j as usize)
                    .and_modify(|x| *x += scratch_count)
                    .or_insert(scratch_count);
            }
        }
    }

    let part2_scratchcount: u32 = scratches.values().sum();

    println!("Part 1 result: {part1_points}");
    println!("Part 2 result: {part2_scratchcount}");
}
