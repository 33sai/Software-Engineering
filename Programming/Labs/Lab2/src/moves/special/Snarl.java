package moves.special;
import ru.ifmo.se.pokemon.*;

public class Snarl extends SpecialMove {
    public Snarl() {
        super(Type.DARK, 55, 0.95);
    }

    @Override
    protected void applyOppEffects(Pokemon p) {
        p.setMod(Stat.SPECIAL_ATTACK, -1);
    }

    @Override
    protected String describe() {
        return "uses Snarl and lowers the Opponents Special Attack by ONE";
    }
    
}
