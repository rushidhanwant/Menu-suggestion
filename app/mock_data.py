from app.schemas.request import RecipeData


async def mock_scraper(link: str):
    return {
        "author": "Erin Clarke",
        "canonical_url": "https://www.wellplated.com/korean-beef-bowl/",
        "category": "Korean",
    }


async def mock_suggestion(recipe_data: RecipeData):
    return {
        "scaled_recipe": {
            "content": "Scaled Ingredients for 9 people:\n\n['2.25 pounds lean ground beef ((I used 93% lean))', '6 tablespoons low sodium soy sauce (plus additional to taste, divided)', '2.25 cups minced scallions (both green and white parts (from about 2 small bundles), divided)', '3 tablespoons minced garlic (about 9 cloves)', '6 tablespoons rice vinegar', '6 tablespoons honey', '6 tablespoons minced or finely grated fresh ginger', '3/4 teaspoon red pepper flakes (plus additional to taste)', '3 tablespoons sesame oil (plus additional to taste)', 'Cooked brown rice (quinoa, or cauliflower rice)', '3.75 cups shredded carrots (see recipe notes to pickle them for an upgrade)', 'Thinly sliced seedless cucumbers (Persian-style or English/hot house)', 'Toasted sesame seeds']",
            "additional_kwargs": {},
            "type": "ai",
            "example": "false"
        },
        "suggested_menu": {
            "content": "Based on the given ingredients and servings, here is a suggested menu:\n\n1. Ground Beef Stir-Fry\n   Ingredients:\n   - 2.25 pounds lean ground beef\n   - 6 tablespoons low sodium soy sauce (plus additional to taste, divided)\n   - 1.5 cups minced scallions (both green and white parts, divided)\n   - 1 tablespoon minced garlic (about 3 cloves)\n   - 2 tablespoons rice vinegar\n   - 2 tablespoons honey\n   - 2 tablespoons minced or finely grated fresh ginger\n   - 1/4 teaspoon red pepper flakes (plus additional to taste)\n   - 1 tablespoon sesame oil (plus additional to taste)\n   - Cooked brown rice (quinoa, or cauliflower rice)\n   \n   Instructions:\n   1. Heat sesame oil in a large skillet over medium heat.\n   2. Add ground beef and cook until browned and cooked through. Drain any excess fat.\n   3. In a small bowl, whisk together soy sauce, rice vinegar, honey, ginger, garlic, and red pepper flakes.\n   4. Pour the sauce over the cooked ground beef and stir to combine.\n   5. Add half of the minced scallions and cook for an additional 2 minutes.\n   6. Serve the stir-fry over cooked brown rice, quinoa, or cauliflower rice.\n   7. Garnish with remaining minced scallions and toasted sesame seeds.\n\n2. Asian Slaw\n   Ingredients:\n   - 3.75 cups shredded carrots\n   - 1 cup thinly sliced seedless cucumbers (Persian-style or English/hot house)\n   - 1/4 cup minced scallions (green parts)\n   - 2 tablespoons rice vinegar\n   - 1 tablespoon low sodium soy sauce\n   - 1 tablespoon honey\n   - 1 tablespoon sesame oil\n   - 1/4 teaspoon red pepper flakes (optional)\n   \n   Instructions:\n   1. In a large bowl, combine shredded carrots, sliced cucumbers, and minced scallions.\n   2. In a small bowl, whisk together rice vinegar, soy sauce, honey, sesame oil, and red pepper flakes (if using).\n   3. Pour the dressing over the vegetable mixture and toss to coat evenly.\n   4. Let the slaw sit for at least 10 minutes to allow the flavors to meld.\n   5. Serve as a side dish or as a topping for the ground beef stir-fry.\n\n3. Pickled Carrots\n   Ingredients:\n   - 3.75 cups shredded carrots\n   - 2 cups rice vinegar\n   - 1 cup water\n   - 1/4 cup granulated sugar\n   - 1 tablespoon salt\n   \n   Instructions:\n   1. In a small saucepan, combine rice vinegar, water, sugar, and salt.\n   2. Heat over medium heat until the sugar and salt have dissolved.\n   3. Place the shredded carrots in a large jar or container.\n   4. Pour the hot vinegar mixture over the carrots, ensuring they are fully submerged.\n   5. Let the carrots pickle in the refrigerator for at least 1 hour, or up to overnight.\n   6. Drain the pickled carrots before using them in the Asian slaw or as a topping for other dishes.\n\nEnjoy your meal!",
            "additional_kwargs": {},
            "type": "ai",
            "example": "false"
        }
    }


def mock_suggestion_data():
    return {'scaled_recipe': {'additional_kwargs': {},
                              'content': 'Scaled Ingredients for 9 people:\n'
                                         '\n'
                                         "['2.25 pounds lean ground beef ((I used 93% "
                                         "lean))', '6.75 tablespoons low sodium soy sauce "
                                         "(plus additional to taste, divided)', '3.375 "
                                         'cups minced scallions (both green and white '
                                         "parts (from about 1 small bundle), divided)', "
                                         "'2.25 tablespoons minced garlic (about 3 "
                                         "cloves)', '4.5 tablespoons rice vinegar', '4.5 "
                                         "tablespoons honey', '4.5 tablespoons minced or "
                                         "finely grated fresh ginger', '0.675 teaspoon "
                                         "red pepper flakes (plus additional to taste)', "
                                         "'2.25 tablespoons sesame oil (plus additional "
                                         "to tase)', 'Cooked brown rice (quinoa, or "
                                         "cauliflower rice)', '2.025 cups shredded "
                                         'carrots (see recipe notes to pickle them for an '
                                         "upgrade)', 'Thinly sliced seedless cucumbers "
                                         "(Persian-style or English/hot house)', 'Toasted "
                                         "sesame seeds']",
                              'example': False,
                              'type': 'ai'},
            'suggested_menu': {'additional_kwargs': {},
                               'content': 'Based on the given ingredients and servings, '
                                          'here is a suggested menu:\n'
                                          '\n'
                                          '1. Beef Stir-Fry\n'
                                          '   Ingredients:\n'
                                          '   - 2.25 pounds lean ground beef (93% lean)\n'
                                          '   - 6.75 tablespoons low sodium soy sauce '
                                          '(plus additional to taste, divided)\n'
                                          '   - 1.125 cups minced scallions (both green '
                                          'and white parts, divided)\n'
                                          '   - 0.75 tablespoon minced garlic (about 1 '
                                          'clove)\n'
                                          '   - 1.5 tablespoons rice vinegar\n'
                                          '   - 1.5 tablespoons honey\n'
                                          '   - 1.5 tablespoons minced or finely grated '
                                          'fresh ginger\n'
                                          '   - 0.225 teaspoon red pepper flakes (plus '
                                          'additional to taste)\n'
                                          '   - 0.75 tablespoon sesame oil (plus '
                                          'additional to taste)\n'
                                          '   - Cooked brown rice, quinoa, or cauliflower '
                                          'rice\n'
                                          '   - 0.675 cup shredded carrots (pickled for '
                                          'an upgrade)\n'
                                          '   - Thinly sliced seedless cucumbers '
                                          '(Persian-style or English/hot house)\n'
                                          '   - Toasted sesame seeds\n'
                                          '\n'
                                          '   Instructions:\n'
                                          '   1. In a large skillet or wok, heat the '
                                          'sesame oil over medium-high heat.\n'
                                          '   2. Add the minced garlic, minced ginger, '
                                          'and red pepper flakes. Cook for about 1 minute '
                                          'until fragrant.\n'
                                          '   3. Add the ground beef and cook until '
                                          'browned and cooked through. Drain any excess '
                                          'fat if necessary.\n'
                                          '   4. In a small bowl, whisk together 6.75 '
                                          'tablespoons of soy sauce, rice vinegar, honey, '
                                          'and 1/2 cup of minced scallions.\n'
                                          '   5. Pour the sauce mixture over the cooked '
                                          'beef and stir to coat evenly. Cook for another '
                                          '2-3 minutes.\n'
                                          '   6. Serve the beef stir-fry over cooked '
                                          'brown rice, quinoa, or cauliflower rice.\n'
                                          '   7. Garnish with pickled shredded carrots, '
                                          'sliced cucumbers, and toasted sesame seeds.\n'
                                          '\n'
                                          '2. Asian Slaw\n'
                                          '   Ingredients:\n'
                                          '   - 3.375 cups shredded cabbage\n'
                                          '   - 1.5 cups shredded carrots\n'
                                          '   - 0.375 cup minced scallions (green parts)\n'
                                          '   - 1.5 tablespoons rice vinegar\n'
                                          '   - 1.5 tablespoons low sodium soy sauce\n'
                                          '   - 1.5 tablespoons honey\n'
                                          '   - 0.75 tablespoon sesame oil\n'
                                          '   - 0.225 teaspoon red pepper flakes\n'
                                          '\n'
                                          '   Instructions:\n'
                                          '   1. In a large bowl, combine the shredded '
                                          'cabbage, shredded carrots, and minced '
                                          'scallions.\n'
                                          '   2. In a separate small bowl, whisk together '
                                          'the rice vinegar, soy sauce, honey, sesame '
                                          'oil, and red pepper flakes.\n'
                                          '   3. Pour the dressing over the cabbage '
                                          'mixture and toss to coat evenly.\n'
                                          '   4. Let the slaw sit for at least 10-15 '
                                          'minutes to allow the flavors to meld.\n'
                                          '   5. Serve the Asian slaw as a side dish or '
                                          'topping for the beef stir-fry.\n'
                                          '\n'
                                          '3. Ginger-Garlic Stir-Fried Vegetables\n'
                                          '   Ingredients:\n'
                                          '   - Assorted vegetables of your choice (such '
                                          'as bell peppers, broccoli, snap peas, carrots, '
                                          'etc.)\n'
                                          '   - 1.125 cups minced scallions (green '
                                          'parts)\n'
                                          '   - 1.5 tablespoons minced garlic (about 2 '
                                          'cloves)\n'
                                          '   - 1.5 tablespoons minced or finely grated '
                                          'fresh ginger\n'
                                          '   - 1.5 tablespoons low sodium soy sauce\n'
                                          '   - 1.5 tablespoons rice vinegar\n'
                                          '   - 0.75 tablespoon honey\n'
                                          '   - 0.75 tablespoon sesame oil\n'
                                          '\n'
                                          '   Instructions:\n'
                                          '   1. Heat the sesame oil in a large skillet '
                                          'or wok over medium-high heat.\n'
                                          '   2. Add the minced garlic and minced ginger. '
                                          'Cook for about 1 minute until fragrant.\n'
                                          '   3. Add the assorted vegetables and stir-fry '
                                          'for 4-5 minutes until crisp-tender.\n'
                                          '   4. In a small bowl, whisk together the soy '
                                          'sauce, rice vinegar, honey, and minced '
                                          'scallions.\n'
                                          '   5. Pour the sauce mixture over the '
                                          'stir-fried vegetables and toss to coat.\n'
                                          '   6. Cook for another 1-2 minutes until the '
                                          'vegetables are coated and heated through.\n'
                                          '   7. Serve the ginger-garlic stir-fried '
                                          'vegetables as a side dish or as a vegetarian '
                                          'option.\n'
                                          '\n'
                                          'Note: Adjust the quantities of ingredients '
                                          'based on the desired number of servings. Enjoy '
                                          'your meal!',
                               'example': False,
                               'type': 'ai'}}
