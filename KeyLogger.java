


import java.awt.event.KeyEvent;

import org.jnativehook.GlobalScreen;
import org.jnativehook.NativeHookException;
import org.jnativehook.keyboard.NativeKeyEvent;
import org.jnativehook.keyboard.NativeKeyListener;

public class RLbot2 implements NativeKeyListener{

	public static void main(String args[]) {

		try {
			GlobalScreen.registerNativeHook();
		} catch (NativeHookException e) {
			// TODO Auto-generated catch block                  
			e.printStackTrace();
		}
			GlobalScreen.getInstance().addNativeKeyListener(new RLbot2());
}
	@Override
	public void nativeKeyPressed(NativeKeyEvent e) {
		KeyCap k = new KeyCap(); 
		if(e.getKeyCode()==KeyEvent.VK_ENTER) {
			System.out.println("");
		}else {
			System.out.print(NativeKeyEvent.getKeyText(e.getKeyCode()));	
		}if(e.getKeyCode()==KeyEvent.VK_CONTROL) {
			System.exit(0);
		}
	
	}

	@Override
	public void nativeKeyReleased(NativeKeyEvent e) {
		// TODO Auto-generated method stub
		//   System.out.println("Released:"+NativeKeyEvent.getKeyText(e.getKeyCode()));
	}

	@Override
	public void nativeKeyTyped(NativeKeyEvent e) {
		// TODO Auto-generated method stub
//		System.out.println(e.getKeyCode() );
	}
	
} 
