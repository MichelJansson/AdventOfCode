use std::{collections::HashMap, fs};

fn main() {
    let input = fs::read_to_string("input.txt").expect("Could not read input.txt");

    let lines: Vec<Vec<char>> = input.lines().map(|f| f.chars().collect()).collect();
    let y_len = lines.len() as isize;
    let x_len = lines[0].len() as isize;

    let mut result = 0;
    let mut gear_candidates: HashMap<(isize, isize), Vec<i32>> = HashMap::new();

    let dirs_xy: [(isize, isize); 8] = [
        (-1, -1),
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
    ];

    for (y, line) in lines.iter().enumerate() {
        let mut num: String = String::new();
        let mut is_partnum = false;
        let mut is_gear_candidate = false;
        let mut adjacent_star = (-1, -1);

        for (x, char) in line.iter().enumerate() {
            if char.is_numeric() {
                num.push(char.clone());

                // Check for adjacent symbols
                for (x_adj, y_adj) in dirs_xy.map(|dir| (x as isize + dir.0, y as isize + dir.1)) {
                    // Dont look outside the vectors
                    if x_adj < 0 || y_adj < 0 || x_adj >= x_len || y_adj >= y_len {
                        continue;
                    }

                    let adjacent_char = lines[y_adj as usize][x_adj as usize];

                    if adjacent_char != '.' && !adjacent_char.is_numeric() {
                        is_partnum = true;
                    }

                    if adjacent_char == '*' {
                        is_gear_candidate = true;
                        adjacent_star = (x_adj, y_adj);
                    }
                }
            }

            // End of partnumber, add it to the totals
            if !char.is_numeric() || x as isize == x_len - 1 {
                if !num.is_empty() {
                    let num = num.parse::<i32>().unwrap();

                    if is_partnum {
                        result += num;
                    }

                    if is_gear_candidate {
                        gear_candidates.entry(adjacent_star).or_insert(Vec::new());
                        gear_candidates
                            .entry(adjacent_star)
                            .and_modify(|f| f.push(num));
                    }
                }

                num.clear();
                is_partnum = false;
                is_gear_candidate = false;
                adjacent_star = (-1, -1);
            }
        }
    }

    println!("Part 1: {result}");

    let result2 = gear_candidates
        .values()
        .filter(|x| x.len() == 2) // Gears is stars with exactly two partnumbers
        .fold(0, |acc, x| acc + (x[0] * x[1]));

    println!("Part 2: {result2}");
}
