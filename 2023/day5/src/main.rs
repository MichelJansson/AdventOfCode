use std::{fs, ops::Range};

fn main() {
    let input = fs::read_to_string("input.txt").expect("Could not read input.txt");
    let mut seeds: Vec<i64> = Vec::new();
    let mut maps: Vec<Vec<(i64, i64, i64)>> = Vec::new();

    // Parse maps
    for (i, section) in input.split(':').skip(1).enumerate() {
        // First section is seeds that has different format
        if i == 0 {
            seeds = section
                .split_whitespace()
                .filter_map(|x| x.parse::<i64>().ok())
                .collect();

            continue;
        }

        let data_points: Vec<i64> = section
            .split_whitespace()
            .filter_map(|x| x.parse::<i64>().ok())
            .collect();

        let mut ranges: Vec<(i64, i64, i64)> = Vec::new();

        for chunk in data_points.chunks(3) {
            ranges.push((chunk[0], chunk[1], chunk[2]));
        }

        maps.push(ranges);
    }

    // Read maps, part 1
    let mut result1_min_location: i64 = i64::MAX;
    for seed in &seeds {
        let location = find_seed_location(seed, &maps);
        result1_min_location = result1_min_location.min(location);
    }
    println!("Result part1: {result1_min_location}");

    // Read maps, part 2
    let mut result2_min_location: i64 = i64::MAX;
    for seed_range in seeds.chunks(2).map(|x| x[0]..x[0] + x[1]) {
        let min_location = find_seed_range_location(seed_range, &maps);

        result2_min_location = result2_min_location.min(min_location);
    }
    println!("Result part2: {result2_min_location}");
}

fn find_seed_location(seed: &i64, maps: &Vec<Vec<(i64, i64, i64)>>) -> i64 {
    let mut current_path: i64 = *seed;

    for map in maps {
        let range = map
            .iter()
            .find(|(_, src, len)| current_path >= *src && current_path < (src + len));

        if range.is_some() {
            let (dst, src, _) = range.unwrap();
            current_path = dst + (current_path - src);
        } else {
            // output = input
        }
    }

    return current_path;
}

fn find_seed_range_location(seed_range: Range<i64>, maps: &Vec<Vec<(i64, i64, i64)>>) -> i64 {
    let mut current_path_ranges: Vec<Range<i64>> = Vec::new();
    current_path_ranges.push(seed_range);

    for map in maps {
        let mut path_ranges_out: Vec<Range<i64>> = Vec::new();

        for current_path in &current_path_ranges {
            // Map ranges that are in range of current path range
            let mut map_ranges: Vec<(Range<i64>, Range<i64>)> = map
                .iter()
                .filter(|(_, src, len)| {
                    (current_path.start >= *src && current_path.start < src + len)
                        || (current_path.end >= *src && current_path.end < src + len)
                })
                .map(|(dst, src, len)| (*dst..dst + len, *src..src + len))
                .collect();

            map_ranges.sort_by_key(|x| x.1.start);

            if map_ranges.is_empty() {
                path_ranges_out.push(current_path.clone());
            } else {
                let mut start = current_path.start;
                let end = current_path.end;

                for (dst, src) in map_ranges {
                    // Lower than range, split and add unmapped
                    if start < src.start {
                        path_ranges_out.push(start..src.start - 1);
                        start = src.start - 1;
                    }

                    // In range
                    if start >= src.start {
                        let from_start = start - src.start;
                        let len = end.min(src.end) - start;
                        path_ranges_out.push(dst.start + from_start..dst.start + from_start + len);
                        start = src.start + from_start + len;
                    }
                }

                // Still some unused numbers
                if start < end {
                    path_ranges_out.push(start..end);
                }
            }
        }
        current_path_ranges = path_ranges_out;
    }

    let min_location = current_path_ranges
        .iter()
        .min_by_key(|x| x.start)
        .unwrap()
        .start;
    min_location
}
