package pokemon.normal;
import ru.ifmo.se.pokemon.*;
import moves.status.Rest;
import moves.special.Flamethrower;
import moves.special.MudBomb;

public class Chansey extends Happiny {
    public Chansey(String name, int level) {
        super(name, level);
        setType(Type.NORMAL);
        setStats(250, 5, 5, 35, 105, 50);
        setMove(new Rest(), new Flamethrower(), new MudBomb());
    }
}