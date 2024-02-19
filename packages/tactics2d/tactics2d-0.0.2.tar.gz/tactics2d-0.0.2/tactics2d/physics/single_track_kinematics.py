##! python3
# -*- coding: utf-8 -*-
# Copyright (C) 2024, Tactics2D Authors. Released under the GNU GPLv3.
# @File: single_track_kinematics.py
# @Description: This file implements a kinematic single-track model for a vehicle.
# @Author: Yueyuan Li
# @Version: 1.0.0

from typing import Tuple

import numpy as np

from .physics_model_base import PhysicsModelBase
from tactics2d.trajectory.element import State


class SingleTrackKinematics(PhysicsModelBase):
    """This class implements a kinematic single-track model for a vehicle. The kinematic single-track model is a simplified model to simulate the vehicle dynamics. It combines the front and rear wheels into a single wheel, and the vehicle is assumed to be a point mass. The assumptions in this implementation include:

    The kinematic single-track model is a simplified model to simulate the vehicle dynamics. It combines the front and rear wheels into a single wheel, and the vehicle is assumed to be a point mass. The assumptions in this implementation include:

    1. The mass of the vehicle is concentrated at the center of the vehicle.
    2. The vehicle is a rigid body.
    3. The vehicle is front-wheel-only.
    4. The vehicle is operating in a 2D plane (x-y).

    This model will lose its accuracy when the time step is set too large or the vehicle is made to travel at a high speed.

    !!! info "Reference"
        Kong, Jason, et al. "Kinematic and dynamic vehicle models for autonomous driving control design." *2015 IEEE intelligent vehicles symposium* (IV). IEEE, 2015.

    Attributes:
        dist_front_hang (float): The distance from the center of the mass to the front axles. The unit is meter.
        dist_rear_hang (float): The distance from the center of the mass to the rear axles. The unit is meter.
        wheel_base (float): The distance between the front and rear axles, which should be the sum of dist_front_hang and dist_rear_hang. The unit is meter.
        steer_range (list): The range of the steering angle. The unit is radian. Defaults to None.
        speed_range (list): The range of the vehicle speed. The unit is meter per second. Defaults to None.
        accel_range (list): The range of the vehicle acceleration. The unit is meter per second squared. Defaults to None.
        delta_t (float): The discrete time step for the simulation. The unit is second. Defaults to MAX_DELTA_T.
    """

    def __init__(
        self,
        dist_front_hang: float,
        dist_rear_hang: float,
        steer_range: Tuple[float, float] = None,
        speed_range: Tuple[float, float] = None,
        accel_range: Tuple[float, float] = None,
        delta_t: float = None,
    ):
        self.dist_front_hang = dist_front_hang
        self.dist_rear_hang = dist_rear_hang
        self.wheel_base = dist_front_hang + dist_rear_hang
        self.speed_range = speed_range
        self.steer_range = steer_range
        self.accel_range = accel_range
        self.delta_t = min(delta_t, self.MIN_DELTA_T) if delta_t is not None else self.DELTA_T

    def _step(self, x, y, heading, speed, accel, steer, dt):
        new_x = x + speed * np.cos(heading) * dt
        new_y = y + speed * np.sin(heading) * dt

        new_heading = heading + speed / self.wheel_base * np.tan(steer) * dt

        new_speed = speed + accel * self.delta_t
        new_speed = np.clip(new_speed, *self.speed_range)

        return new_x, new_y, new_heading, new_speed

    def step(self, state: State, action: Tuple[float, float], step: float) -> Tuple[State, tuple]:
        """Update the state of a vehicle with the Kinematic Single-Track Model.

        Args:
            state (State): The current state of the vehicle.
            action (list): The action to be applied to the vehicle. The action is a two-element
                tuple [steer, accel]. The steer is the steering angle, and the accel is the
                acceleration. The unit of the steer is radian, and the unit of the accel is
                meter per second squared.
            step (float): The length of the step for the simulation. The unit is second.

        Returns:
            State: The new state of the vehicle.
            tuple: The action that was executed.
        """
        steer, accel = action
        x, y, heading, speed = state.x, state.y, state.heading, state.speed
        # here we use rear axle center to update
        rear_center_x, rear_center_y = x - self.dist_rear_hang * np.cos(
            heading
        ), y - self.dist_rear_hang * np.sin(heading)
        speed, accel = accel, 0  # TODO

        if self.steer_range is not None:
            steer = np.clip(steer, *self.steer_range)

        if self.accel_range is not None:
            accel = np.clip(accel, *self.accel_range)

        # The angle of the current velocity of the center of mass with respect to the longitudinal axis of the car.
        dt = self.delta_t
        while dt <= step:
            rear_center_x, rear_center_y, heading, speed = self._step(
                rear_center_x, rear_center_y, heading, speed, accel, steer, self.delta_t
            )
            dt += self.delta_t

        if dt > step:
            rear_center_x, rear_center_y, heading, speed = self._step(
                rear_center_x,
                rear_center_y,
                heading,
                speed,
                accel,
                steer,
                step - (dt - self.delta_t),
            )
        # recover the geometry center from rear axle center
        x = rear_center_x + self.dist_rear_hang * np.cos(heading)
        y = rear_center_y + self.dist_rear_hang * np.sin(heading)
        new_state = State(
            state.frame + int(step * 1000), x=x, y=y, heading=heading, speed=speed, accel=accel
        )

        return new_state, (steer, accel)

    def verify_state(self, curr_state: State, prev_state: State) -> bool:
        return True
