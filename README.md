# Characteristics

Version: 0.0
Name: Arduino language
Extentions: *.adn
But: control the aduino whit language

# Example code (hello world)
```py
[0] # hello world on ADN language
[1] Output > "hello world"
```
# Example code (minor or major)
```py
[0] # minor or major on ADN language
[1] $years = Input > "Years: "
[2] if $years < 18 {
[3]    Output > "you are minor"
[4] }
[5] else {
[6]     Output > "you are major"
[7] }
```
# Example code (structure class)
[0] # structure class on ADN language
[1] class $player {
[2]     func $init <$username, $health> {
[3]       $this : $username = $username           $this : $health = $health  
[4]     }
[5]     func $move <$position> {
[6]         Output > "player moved !"
[7]     }
[8] }
[9]
[10] $player1 = new $player > "Wolf", 10
[11] $player1 : $move > [0, 0]
