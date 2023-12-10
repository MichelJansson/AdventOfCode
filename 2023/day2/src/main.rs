use std::collections::HashMap;
use std::fs;

fn main() {
    // Input data
    let input = fs::read_to_string("input.txt").unwrap();

    // Number of cubes for each color
    let red_cubes = 12;
    let green_cubes = 13;
    let blue_cubes = 14;

    // Parse input and simulate games
    let possible_games: Vec<_> = input
        .lines()
        .filter_map(|line| parse_game(line))
        .filter(|game| game.is_possible(red_cubes, green_cubes, blue_cubes))
        .map(|game| game.id)
        .collect();

    // Calculate the sum of IDs of possible games
    let sum_of_ids: usize = possible_games.iter().sum();
    // Print the result
    println!("Sum of IDs of possible games: {}", sum_of_ids);

    // Parse input and find the sum of powers
    let sum_of_powers: usize = input
        .lines()
        .filter_map(|line| parse_game(line))
        .map(|game| game.min_set_power())
        .sum();

    // Print the result
    println!("Sum of powers of minimum sets: {}", sum_of_powers);
}

struct Game {
    id: usize,
    subsets: Vec<Vec<(usize, String)>>,
}

impl Game {
    fn new(id: usize, subsets: Vec<Vec<(usize, String)>>) -> Self {
        Game { id, subsets }
    }

    fn is_possible(&self, red_cubes: usize, green_cubes: usize, blue_cubes: usize) -> bool {
        let max_cube_counts = self.max_cube_counts();

        *max_cube_counts.get("red").unwrap_or(&0) <= red_cubes
            && *max_cube_counts.get("green").unwrap_or(&0) <= green_cubes
            && *max_cube_counts.get("blue").unwrap_or(&0) <= blue_cubes
    }

    fn min_set_power(&self) -> usize {
        let max_cube_counts = self.max_cube_counts();
        max_cube_counts["red"] * max_cube_counts["green"] * max_cube_counts["blue"]
    }

    fn max_cube_counts(&self) -> HashMap<&str, usize> {
        let mut max_cube_counts: HashMap<&str, usize> = HashMap::new();

        for subset in &self.subsets {
            for &(count, ref color) in subset {
                *max_cube_counts.entry(color.as_str()).or_insert(0) =
                    count.max(*max_cube_counts.get(color.as_str()).unwrap_or(&0));
            }
        }

        return max_cube_counts;
    }
}

fn parse_game(input: &str) -> Option<Game> {
    let parts: Vec<&str> = input.split(": ").collect();

    if parts.len() == 2 {
        let id_str = parts[0].trim().strip_prefix("Game ")?;
        let id = id_str.parse().ok()?;

        let subsets_str = parts[1];
        let subsets: Vec<Vec<(usize, String)>> = subsets_str
            .split(';')
            .map(|subset| {
                subset
                    .trim()
                    .split(',')
                    .map(|s| {
                        let parts: Vec<&str> = s.trim().split_whitespace().collect();
                        if parts.len() == 2 {
                            let count = parts[0].parse().ok()?;
                            let color = parts[1].to_string();
                            Some((count, color))
                        } else {
                            None
                        }
                    })
                    .collect::<Option<Vec<(usize, String)>>>()
            })
            .collect::<Option<Vec<Vec<(usize, String)>>>>()?;

        Some(Game::new(id, subsets))
    } else {
        None
    }
}
