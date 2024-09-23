my_dict = {
    "mijas": [
        {
            "name": "go shopping",
            "description": "sakjdjs fdjvbfdjvs dcdsvfvhef vds",
            "due_date": "2040/12/02",
            "priority": "low",
            "completed": False
        },
        {
            "name": "go to smoke",
            "description": "smoking marijuna by sitting in the lake side",
            "due_date": "2024/10/29",
            "priority": "medium",
            "completed": False
        }
    ],
    "rojan": [
        {
            "name": "going gym",
            "description": "go to gym for the shoulder recovery.",
            "due_date": "2025/04/03",
            "priority": "high",
            "completed": False
        },
        {
            "name": "learn pytho",
            "description": "need to learn some ml algos",
            "due_date": "2026/04/03",
            "priority": "high",
            "completed": False
        }
    ],
    "manami": [
        {
            "name": "going saloon",
            "description": "need to go salonn to make my hair",
            "due_date": "2024/10/09",
            "priority": "low",
            "completed": False
        }
    ]
}

for task in my_dict["rojan"]:
    print(f"Task Name: {task['name']}")
    print(f"Description: {task['description']}")
    print(f"Due Date: {task['due_date']}")
    print(f"Priority: {task['priority']}")
    print(f"Completed: {task['completed']}")
    print("-" * 40)
