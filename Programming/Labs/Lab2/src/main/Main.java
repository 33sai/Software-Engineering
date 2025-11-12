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
        battle.addAlly(new Stantler("", 1));
        battle.addAlly(new Corphish("", 1));
        battle.addAlly(new Crawdaunt("", 1));

        // Team 2: Normal Types
        battle.addFoe(new Happiny("", 1));
        battle.addFoe(new Chansey("", 1));
        battle.addFoe(new Blissey("", 1));

        battle.go();
    }
}