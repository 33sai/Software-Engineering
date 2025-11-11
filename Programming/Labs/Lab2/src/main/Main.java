package main;

import ru.ifmo.se.pokemon.*;
import pokemon.normal.Stantler;
import pokemon.normal.Happiny;
import pokemon.normal.Chansey;
import pokemon.normal.Blissey;
import pokemon.water.Corphish;
import pokemon.water.Crawdaunt;

public class Main {
    public static void main(String[] args) {
        Battle battle = new Battle();

        // Team 1: Water Types and Normal Type
        battle.addAlly(new Corphish("Corphish", 1));
        battle.addAlly(new Crawdaunt("Crawdaunt", 1));
        battle.addAlly(new Stantler("Stantler", 1));

        // Team 2: Normal Types
        battle.addFoe(new Happiny("Happiny", 1));
        battle.addFoe(new Chansey("Chansey", 1));
        battle.addFoe(new Blissey("Blissey", 1));

        battle.go();
    }
}