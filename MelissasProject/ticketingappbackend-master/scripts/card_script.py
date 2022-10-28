from models.Card import Card


def getCardsByCategory(db, categoryID):
    return db.query(Card).filter(Card.category_id == categoryID).all()


def addCard(db, payload):

    # cards = getCardsByCategory(db, payload.category_id)

    # rank = max(cards, key=lambda x : x["rank"]) if len(cards) + 1 > 0 else 1

    card = Card(text=payload.text, rank=payload.rank,
                category_id=payload.category_id)
    db.add(card)
    db.commit()
    db.refresh(card)
    return card


def removeCard(db, cardID):
    db.query(Card).filter(Card.id == cardID).delete()
    db.commit()
    return True


def updateCardText(db, payload):

    db.query(Card).filter(Card.id == payload.id).update({
        "text": payload.text,
    })

    db.commit()

    return True


def updateCardRank(db, cards):

    # to update card's category and rank when dragged from one category to other

    for card in cards:
         db.query(Card).filter(Card.id == card["id"]).update({
            "rank": card["rank"],
            "category_id": card["category_id"]
        })

    db.commit()

    return True
