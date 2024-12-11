#include <SFML/Graphics.hpp>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    setlocale(LC_ALL, "Rus");
    cout << "Введите размерность матрицы" << endl;
    int n;
    cin >> n;

    const int cellSize = 50; // Размер одной ячейки
    const int padding = 5;   // Отступ между ячейками

    // Вычисление размера окна
    int windowSize = n * (cellSize + padding);

    // Создание окна
    sf::RenderWindow window(sf::VideoMode(windowSize, windowSize), "OMG?!?!?");

    // Массив для хранения клеток
    vector<vector<sf::RectangleShape>> grid(n, vector<sf::RectangleShape>(n));

    // Инициализация клеток
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            grid[i][j].setSize(sf::Vector2f(cellSize, cellSize));
            grid[i][j].setPosition(j * (cellSize + padding), i * (cellSize + padding));
            grid[i][j].setFillColor(sf::Color::Green); // Белый цвет по умолчанию
            grid[i][j].setOutlineThickness(1.0f);
            grid[i][j].setOutlineColor(sf::Color::Black);
        }
    }

    // Главный цикл
    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        // Очистка окна
        window.clear(sf::Color::Black);

        // Отображение клеток
        if (n % 2 == 0) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    for (int m = 0; m < (n / 2) + 1; m++)
                    {

                        if (j - i == (n / 2) + m) {
                            grid[i][j].setFillColor(sf::Color::White);
                        }
                        else if (j + i == (n / 2) - 1 - m) {
                            grid[i][j].setFillColor(sf::Color::White);
                        }
                        else if (i == (n / 2) + 1 + m) {
                            grid[i][j].setFillColor(sf::Color::White);
                        }
                        window.draw(grid[i][j]);
                    }
                }
            }
        } 
        else {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    for (int m = 0; m < (n / 2) + 1; m++)
                    {

                        if (j - i == (n / 2) + m) {
                            grid[i][j].setFillColor(sf::Color::White);
                        }
                        else if (j + i == (n / 2) - m) {
                            grid[i][j].setFillColor(sf::Color::White);
                        }
                        else if (i == (n / 2) + 2 + m) {
                            grid[i][j].setFillColor(sf::Color::White);
                        }
                        window.draw(grid[i][j]);
                    }
                }
            }

        }

        // Отображение изменений
        window.display();
    }

    return 0;
}