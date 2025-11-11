package pokemon.water;
import ru.ifmo.se.pokemon.*;
import moves.physical.CrabHammer;
import moves.special.BubbleBeam;
import moves.status.Swagger;
import moves.special.Snarl;

public final class Crawdaunt extends Corphish {
    public Crawdaunt(String name, int level) {
        super(name, level);
        setType(Type.WATER, Type.DARK);
        setStats(63, 120, 85, 90, 55, 55);
        setMove(new CrabHammer(), new BubbleBeam(), 
            new Swagger(), new Snarl());
        

    }
}
