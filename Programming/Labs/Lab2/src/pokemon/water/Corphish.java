package pokemon.water;
import ru.ifmo.se.pokemon.*;
import moves.physical.CrabHammer;
import moves.special.BubbleBeam;
import moves.status.Swagger;

public class Corphish extends Pokemon {
    public Corphish(String name, int level) {
        super(name, level);
        setType(Type.WATER);
        setStats(43, 80, 65, 50, 35, 35);
        setMove(new CrabHammer(), new BubbleBeam(), new Swagger());
    }
    
}
