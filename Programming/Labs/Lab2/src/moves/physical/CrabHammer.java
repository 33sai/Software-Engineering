package moves.physical;
import ru.ifmo.se.pokemon.*;
public class CrabHammer extends PhysicalMove {
    public CrabHammer() {
        super(Type.WATER, 100, 0.9);
    }

    @Override
    protected double calcCriticalHit(Pokemon att, Pokemon def) {
        return 1.5;
    }

    @Override
    protected String describe() {
        return "uses Crab Hammer";
    }
    
}
