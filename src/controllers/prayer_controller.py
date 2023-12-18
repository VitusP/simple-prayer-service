# /app/src/controllers/prayers_controller.py
from flask import Blueprint, jsonify
from ..service.prayer_service import get_random_prayer
import boto3

prayer_bp = Blueprint("prayer", __name__)


@prayer_bp.route("/prayer")
def get_prayer():
    prayer = get_random_prayer()
    if prayer is not None:
        return (
            jsonify(
                {"PrayerTitle": prayer.get_title(), "PrayerText": prayer.get_text()}
            ),
            200,
        )
    else:
        return jsonify({"error": "Unable to return a prayer"}), 500
