#include <iostream>
#include <cassert>
#include <algorithm>
#include <vector>

struct Event {
    int time;
    int priority;
};

bool compareEvents(const Event& left, const Event& right){
    if (left.time != right.time){
        return left.time < right.time;
    }

    return left.priority > right.priority;
}

std::vector<Event> readEvents(){
    int eventCount;
    std::cin >> eventCount;

    assert(eventCount >= 0);

    std::vector<Event> events;

    for(int i = 0; i < eventCount; i++){
        Event event;
        std::cin >> event.time >> event.priority;
        events.push_back(event);
    }

    return events;
}

void printEvents(const std::vector<Event>& events,
                std::ostream& output){
    for(const Event& event : events){
        output << event.time << " " << event.priority << '\n';
    }
}

void solve(){
    std::vector<Event> events = readEvents();

    std::cerr << "Before sort: \n";
    printEvents(events, std::cerr);

    std::sort(events.begin(), events.end(), compareEvents);

    std::cerr << "After sort: \n";
    printEvents(events, std::cerr);

    printEvents(events, std::cout);
}

int main(){
    solve();
    return 0;
}