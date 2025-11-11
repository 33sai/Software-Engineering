package moves.status;
import ru.ifmo.se.pokemon.*;

public class Rest extends StatusMove {
    public Rest() {
        super(Type.PSYCHIC, 0, 0);
    }

    @Override
    protected void applySelfEffects(Pokemon p) {
        Effect sleepEffect = new Effect().condition(Status.SLEEP).turns(2);
        p.setCondition(sleepEffect);
        p.restore();
    }

    @Override
    protected String describe() {
        return "uses Rest to go to bed mid-match and heal";
    }
    
}
