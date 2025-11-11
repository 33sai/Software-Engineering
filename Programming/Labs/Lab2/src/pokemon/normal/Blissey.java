package pokemon.normal;
import ru.ifmo.se.pokemon.*;
import moves.status.Rest;
import moves.special.Flamethrower;
import moves.special.MudBomb;
import moves.physical.TakeDown;

public class Blissey extends Chansey {
    public Blissey(String name, int level) {
        super(name, level);
        setType(Type.NORMAL);
        setStats(255, 10, 10, 75, 135, 55);
        setMove(new Rest(), new Flamethrower(), 
                new MudBomb(), new TakeDown());
    }
}