import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.HashMap;
import java.util.Map;

class CreateLoginForm extends JFrame implements ActionListener {
    JButton b1, b2;
    JPanel newPanel;
    JLabel userLabel, passLabel;
    final JTextField textField1, textField2;

    private Map<String, String> userCredentials;

    CreateLoginForm() {
        userCredentials = new HashMap<>();

        userLabel = new JLabel();
        userLabel.setText("Username");
        textField1 = new JTextField(15);

        passLabel = new JLabel();
        passLabel.setText("Password");
        textField2 = new JPasswordField(15);

        b1 = new JButton("LOGIN");
        b2 = new JButton("CREATE ACCOUNT");

        newPanel = new JPanel(new GridLayout(4, 1));
        newPanel.add(userLabel);
        newPanel.add(textField1);
        newPanel.add(passLabel);
        newPanel.add(textField2);
        newPanel.add(b1);
        newPanel.add(b2);

        add(newPanel, BorderLayout.CENTER);

        b1.addActionListener(this);
        b2.addActionListener(this);
        setTitle("LOGIN FORM");
    }

    public void actionPerformed(ActionEvent ae) {
        String userValue = textField1.getText();
        String passValue = textField2.getText();

        if (ae.getSource() == b1) {
            authenticateUser(userValue, passValue);
        } else if (ae.getSource() == b2) {
            createUser();
        }
    }

    private void authenticateUser(String username, String password) {
        if (userCredentials.containsKey(username) && userCredentials.get(username).equals(password)) {
            SwingUtilities.invokeLater(() -> {
                NewPage page = new NewPage(username);
                page.setVisible(true);
            });
            dispose();
        } else {
            JOptionPane.showMessageDialog(this, "Invalid username or password", "Login Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void createUser() {
        String newUsername = JOptionPane.showInputDialog(this, "Enter a new username:");
        String newPassword = JOptionPane.showInputDialog(this, "Enter a new password:");

        if (newUsername != null && newPassword != null && !newUsername.isEmpty() && !newPassword.isEmpty()) {
            if (!userCredentials.containsKey(newUsername)) {
                userCredentials.put(newUsername, newPassword);
                JOptionPane.showMessageDialog(this, "Account created successfully", "Account Creation", JOptionPane.INFORMATION_MESSAGE);
            } else {
                JOptionPane.showMessageDialog(this, "Username already exists", "Account Creation Error", JOptionPane.ERROR_MESSAGE);
            }
        } else {
            JOptionPane.showMessageDialog(this, "Invalid username or password", "Account Creation Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    public static void main(String arg[]) {
        SwingUtilities.invokeLater(() -> {
            CreateLoginForm form = new CreateLoginForm();
            form.setSize(300, 150);
            form.setVisible(true);
            form.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        });
    }
}
