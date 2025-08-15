#include <iostream>
#include <vector>
#include <string>
#include <algorithm> // For std::max

// Base Spell class
class Spell {
protected:
    std::string scrollName;
public:
    Spell(std::string name = "") : scrollName(name) {}
    virtual ~Spell() {}
    std::string revealScrollName() { return scrollName; }
};

// Derived Fireball class
class Fireball : public Spell {
private:
    int power;
public:
    Fireball(int p) : power(p) {}
    void revealFirepower() {
        std::cout << "Fireball: " << power << std::endl;
    }
};

// ... (Similar derived classes for Frostbite, Waterbolt, Thunderstorm)

// SpellJournal class
class SpellJournal {
public:
    static std::string journal;
    static std::string read() { return journal; }
};
std::string SpellJournal::journal = ""; // Static member initialization

// counterspell function
void counterspell(Spell *spell) {
    // Use dynamic_cast to identify specific spell types
    Fireball *fb = dynamic_cast<Fireball*>(spell);
    if (fb) {
        fb->revealFirepower();
        return;
    }
    // ... (Similar checks for other specific spell types)

    // Handle generic spells (LCS)
    std::string spellName = spell->revealScrollName();
    std::string journalContent = SpellJournal::read();

    int n = spellName.size();
    int m = journalContent.size();
    std::vector<std::vector<int>> dp(n + 1, std::vector<int>(m + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (spellName[i - 1] == journalContent[j - 1]) {
                dp[i][j] = 1 + dp[i - 1][j - 1];
            } else {
                dp[i][j] = std::max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    std::cout << dp[n][m] << std::endl;
}

// Wizard class and main function for input handling
class Wizard {
public:
    Spell *cast() {
        std::string s;
        std::cin >> s;
        int power;
        std::cin >> power; // Read power even if it's for a generic spell (unused)

        if (s == "fire") {
            return new Fireball(power);
        } else if (s == "frost") {
            // ... (return new Frostbite, etc.)
        } else { // Generic spell
            SpellJournal::journal = s; // The problem statement implies the generic spell name is stored in journal
            return new Spell(s);
        }
    }
};

int main() {
    int T;
    std::cin >> T;
    Wizard Arawn;
    while (T--) {
        Spell *spell = Arawn.cast();
        counterspell(spell);
        delete spell; // Important to free memory
    }
    return 0;
}
