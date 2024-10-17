data Nat = Zero | Succ Nat deriving (Eq, Ord)
instance Show Nat where
    show = show.nat_to_int

plus :: Nat -> Nat -> Nat
plus Zero x = x
plus (Succ x) y = plus x (Succ y)

mult :: Nat -> Nat -> Nat
mult Zero _ = Zero
mult (Succ x) y = plus (mult x y) y

nat_to_int :: Nat -> Int
nat_to_int Zero = 0
nat_to_int (Succ x) = 1 + (nat_to_int x)
x = Succ (Succ (Succ Zero))
y = Succ Zero
z = Succ (Succ Zero)

main = print(x)