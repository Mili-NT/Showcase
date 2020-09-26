{--
Lanugage: Haskell
Compiler: GHC

Purpose: Converting strings to bits, and checking if bit values are set.
--}
-- Declares a function, toBits, that takes an array of Chars and outputs a nested array of Chars
toBits :: [Char] -> [[Char]]
-- Declares a function, isSet, that takes two Int values and an array of Chars and outputs a Bool
isSet :: Int -> Int -> [Char] -> Bool

-- test is a ternary implementation bound to ?
test ? t = if test then const t else \f -> f

-- toBits takes an array `xs` and converts it to a nested array containing the bit values for each byte in `xs`
toBits xs | null xs = [] | otherwise = [[show $ ((x `shiftR` i) .&. 1) | i <- [1..8]] >>= id | x <- [ord x | x <- xs]]
-- isSet checks if a specific bit at position `x` in byte at position `y` in the array `xs`
isSet x y xs | null xs = False | or [x > 8, y > length xs] = False | otherwise = (\x -> (x == 1) ? True $ False) (read $ [toBits xs !! x !! y]::Int)