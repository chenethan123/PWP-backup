import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;

class NewPage extends JFrame {
    private JLabel vidLabel, feedLabel;
    private Canvas videoCanvas;
    private JButton forwardButton, backButton, rightButton, leftButton, stopButton, logoutButton;

    NewPage(String username) {
        setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);
        setTitle("Control");
        setSize(510, 510);
        setLocationRelativeTo(null);

        // Create components
        vidLabel = new JLabel("Video");
        vidLabel.setHorizontalAlignment(JLabel.CENTER);

        videoCanvas = new Canvas();
        videoCanvas.setSize(200, 200);
        videoCanvas.setBackground(Color.BLACK);

        feedLabel = new JLabel("No Feed");
        feedLabel.setHorizontalAlignment(JLabel.CENTER);

        forwardButton = new JButton("Forward");
        backButton = new JButton("Backward");
        rightButton = new JButton("Right");
        leftButton = new JButton("Left");
        stopButton = new JButton("Stop");
        logoutButton = new JButton("Logout");

        // Set button actions
        forwardButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                sendRequest("forward");
            }
        });

        backButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                sendRequest("backward");
            }
        });

        rightButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                sendRequest("right");
            }
        });

        leftButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                sendRequest("left");
            }
        });

        stopButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                sendRequest("stop");
            }
        });

        logoutButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                dispose(); // Close the NewPage on logout
            }
        });

        // Set layout
        setLayout(new GridLayout(3, 3));

        // Add components to the frame
        add(vidLabel);
        add(new JLabel()); // Empty cell
        add(feedLabel);
        add(videoCanvas);
        add(forwardButton);
        add(backButton);
        add(rightButton);
        add(leftButton);
        add(stopButton);
        add(logoutButton);

        // Display a message saying "Welcome, username"
        JOptionPane.showMessageDialog(this, "Welcome, " + username, "Logged in!", JOptionPane.INFORMATION_MESSAGE);
    }

    // Function to send requests to the API
    private void sendRequest(String direction) {
        try {
            URL url = new URL("http://192.168.1.25:5000");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("POST");
            connection.setDoOutput(true);

            // Send JSON data
            String jsonInputString = "{\"command\": \"" + direction + "\"}";
            try (OutputStream os = connection.getOutputStream()) {
                byte[] input = jsonInputString.getBytes(StandardCharsets.UTF_8);
                os.write(input, 0, input.length);
            }

            // Check the response if needed

            connection.disconnect();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            NewPage page = new NewPage("TestUser");
            page.setVisible(true);
        });
    }
}
