import random
PROGRAM START

FUNCTION get_cpu_choice():
    cpu_choice = randome choice from "rock, paper, and scissors"
    RETURN cpu_choice
END FUNCTION

FUNCTION get_player_choice():
    WHILE True:
        INPUT player_choice
            IF player_choice is valid THEN:
                RETURN player_choice
            END IF
    END WHILE
END FUNCTION

FUNCTION check_winner(cpu_choice, player_choice):
    IF player_choice == cpu_choice THEN:
        winner = "Tie"
    ELSE IF cpu_choice == "rock" THEN:
        IF player_choice == "paper" THEN:
            winner = "PLAYER"
        ELSE:
            winner = "CPU"
        END IF
    ELSE IF cpu_choice == "paper" THEN:
        IF player_choice == "scissors" THEN:
            winner = "PLAYER"
        ELSE:
            winner = "CPU"
        END IF
    ELSE IF player_choice == "paper" THEN:
        winner = "CPU"
    ELSE:
        winner = "PLAYER"
    END IF
    RETURN winner
END FUNCTION

cpu_choice = get_cpu_choice()

player_choice = get_player_choice()

winner = check_winner(cpu_choice, player_choice)

OUTPUT winner

PROGRAM END
# Random float between 0 and 1
value = random.random()
# Random integer where 1 <= integer <= 10
value = random.randint(1, 10)
# Random choice between "Left" or "Right"
value = random.choice(["Left", "Right"])

# Another valid syntax for random choice
choices = ["Left", "Right"]
value = random.choice(choices)