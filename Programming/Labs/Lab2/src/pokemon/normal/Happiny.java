package pokemon.normal;
import ru.ifmo.se.pokemon.*;
import moves.status.Rest;
import moves.special.Flamethrower;

public class Happiny extends Pokemon {
    public Happiny(String name, int level) {
        super(name, level);
        setType(Type.NORMAL);
        setStats(100, 5, 5, 15, 65, 30);
        setMove(new Rest(), new Flamethrower());
    }
}