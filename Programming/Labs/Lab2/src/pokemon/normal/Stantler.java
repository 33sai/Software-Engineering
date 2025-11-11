package pokemon.normal;
import ru.ifmo.se.pokemon.*;
import moves.status.DoubleTeam;
import moves.special.Extrasensory;
import moves.status.Swagger;
import moves.physical.Tackle;
public final class Stantler extends Pokemon {
    public Stantler(String name, int level) {
        super(name, level);
        setType(Type.NORMAL);
        setStats(73, 95, 62, 85, 65, 85);
        setMove(new DoubleTeam(), new Extrasensory(), 
                new Swagger(), new Tackle());
    }
    
}
