"""
Analytics Brief - Boston Dynamics Spot Enterprise
Python script to generate purchase funnel visualization
"""

import sys
import io
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Configure UTF-8 output for Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Color scheme - Boston Dynamics brand colors
COLOR_PRIMARY = '#009999'  # Teal
COLOR_SECONDARY = '#FFB81C'  # Boston Dynamics yellow/orange
COLOR_HIGHLIGHT = '#003D5C'  # Dark blue
COLOR_LIGHT = '#E6F5F5'  # Light teal

print("="*80)
print("BOSTON DYNAMICS SPOT ENTERPRISE - ANALYTICS BRIEF")
print("Energy & Utilities Division")
print("="*80)

# ================================================================================
# PURCHASE FUNNEL VISUALIZATION FOR B2B ENTERPRISE
# ================================================================================

fig, ax = plt.subplots(figsize=(18, 10))
ax.set_xlim(0, 11)
ax.set_ylim(0, 12)
ax.axis('off')

# Title
ax.text(5.5, 11.5, 'Purchase Process Funnel',
        ha='center', va='top', fontsize=24, fontweight='bold', color=COLOR_HIGHLIGHT)

# Funnel stages (columns)
stages = ['Awareness', 'Interest', 'Consideration', 'Decision', 'Post-Purchase']
stage_x = [2.5, 4.0, 5.5, 7.0, 8.5]

# Draw stage headers
for i, (stage, x) in enumerate(zip(stages, stage_x)):
    ax.text(x, 10.5, stage, ha='center', va='center',
            fontsize=11, fontweight='bold', color=COLOR_HIGHLIGHT)

# Channels (rows)
channels = [
    'Website/SEO',
    'Industry Events',
    'Case Studies',
    'Demo Request',
    'Partner Network',
    'Direct Sales',
    'Webinars',
    'Trade Publications',
    'LinkedIn (B2B)',
    'Email Campaigns',
    'Pilot Program'
]

# Channel positions
y_positions = np.linspace(9.5, 1.5, len(channels))

# Draw "Channels" header
ax.text(1.0, 10.5, 'Channels', ha='center', va='center',
        fontsize=11, fontweight='bold', color=COLOR_HIGHLIGHT)

# Draw channel labels (right-aligned for better appearance)
max_channel_width = max(len(ch) for ch in channels)
for i, (channel, y) in enumerate(zip(channels, y_positions)):
    ax.text(1.8, y, channel, ha='right', va='center',
            fontsize=10, fontweight='bold', color='#333')

# Define which channels are active in which stages
# Format: (channel_index, stage_index, color)
channel_stage_mapping = [
    # Website/SEO
    (0, 0, COLOR_SECONDARY),  # Awareness
    (0, 1, COLOR_PRIMARY),     # Interest

    # Industry Events
    (1, 0, COLOR_PRIMARY),     # Awareness
    (1, 1, COLOR_SECONDARY),   # Interest

    # Case Studies
    (2, 1, COLOR_PRIMARY),     # Interest
    (2, 2, COLOR_SECONDARY),   # Consideration

    # Demo Request
    (3, 2, COLOR_PRIMARY),     # Consideration
    (3, 3, COLOR_SECONDARY),   # Decision

    # Partner Network
    (4, 1, COLOR_SECONDARY),   # Interest
    (4, 2, COLOR_PRIMARY),     # Consideration

    # Direct Sales
    (5, 2, COLOR_SECONDARY),   # Consideration
    (5, 3, COLOR_PRIMARY),     # Decision

    # Webinars
    (6, 1, COLOR_PRIMARY),     # Interest
    (6, 2, COLOR_SECONDARY),   # Consideration

    # Trade Publications
    (7, 0, COLOR_SECONDARY),   # Awareness

    # LinkedIn (B2B)
    (8, 0, COLOR_PRIMARY),     # Awareness
    (8, 1, COLOR_SECONDARY),   # Interest

    # Email Campaigns
    (9, 1, COLOR_PRIMARY),     # Interest
    (9, 2, COLOR_SECONDARY),   # Consideration

    # Pilot Program
    (10, 3, COLOR_PRIMARY),    # Decision
    (10, 4, COLOR_SECONDARY),  # Post-Purchase
]

# Draw boxes for channel-stage intersections
box_width = 1.2
box_height = 0.6

for channel_idx, stage_idx, color in channel_stage_mapping:
    x = stage_x[stage_idx] - box_width/2
    y = y_positions[channel_idx] - box_height/2

    rect = FancyBboxPatch((x, y), box_width, box_height,
                          boxstyle="round,pad=0.05",
                          facecolor=color, edgecolor='black', linewidth=1.5, alpha=0.7)
    ax.add_patch(rect)

# Arrow colors - complementary to teal (#009999): blue, purple, red
ARROW_COLOR_1 = '#3366CC'  # Blue
ARROW_COLOR_2 = '#9933FF'  # Purple
ARROW_COLOR_3 = '#FF3333'  # Red

# Draw customer journey paths (3 example paths)
# Path 1: Website → Demo → Pilot → Purchase
path1_points = [
    (stage_x[0], y_positions[0]),  # Website Awareness
    (stage_x[1], y_positions[0]),  # Website Interest
    (stage_x[2], y_positions[3]),  # Demo Consideration
    (stage_x[3], y_positions[3]),  # Demo Decision
    (stage_x[4], y_positions[10]), # Pilot Post-Purchase
]

# Path 2: Industry Event → Case Study → Sales → Pilot
path2_points = [
    (stage_x[0], y_positions[1]),  # Event Awareness
    (stage_x[1], y_positions[1]),  # Event Interest
    (stage_x[2], y_positions[2]),  # Case Study Consideration
    (stage_x[3], y_positions[5]),  # Direct Sales Decision
    (stage_x[4], y_positions[10]), # Pilot Post-Purchase
]

# Path 3: LinkedIn → Webinar → Partner → Pilot
path3_points = [
    (stage_x[0], y_positions[8]),  # LinkedIn Awareness
    (stage_x[1], y_positions[6]),  # Webinar Interest
    (stage_x[2], y_positions[4]),  # Partner Consideration
    (stage_x[3], y_positions[10]), # Pilot Decision
]

# Draw paths with new colors
for i in range(len(path1_points)-1):
    arrow = FancyArrowPatch(path1_points[i], path1_points[i+1],
                           arrowstyle='->', mutation_scale=20, linewidth=3,
                           color=ARROW_COLOR_1, alpha=0.9, zorder=10)
    ax.add_patch(arrow)

for i in range(len(path2_points)-1):
    arrow = FancyArrowPatch(path2_points[i], path2_points[i+1],
                           arrowstyle='->', mutation_scale=20, linewidth=3,
                           color=ARROW_COLOR_2, alpha=0.9, zorder=10)
    ax.add_patch(arrow)

for i in range(len(path3_points)-1):
    arrow = FancyArrowPatch(path3_points[i], path3_points[i+1],
                           arrowstyle='->', mutation_scale=20, linewidth=3,
                           color=ARROW_COLOR_3, alpha=0.9, zorder=10)
    ax.add_patch(arrow)

# Add legend for journey paths
legend_y = 0.8
ax.text(0.2, legend_y, 'Customer Journey Examples:',
        ha='left', va='center', fontsize=10, fontweight='bold', style='italic',
        color=COLOR_HIGHLIGHT)

# Legend items with arrows (using new colors)
legend_items = [
    ('Path 1: Web → Demo → Pilot', ARROW_COLOR_1),
    ('Path 2: Event → Sales → Pilot', ARROW_COLOR_2),
    ('Path 3: Social → Webinar → Partner', ARROW_COLOR_3)
]

for i, (label, color) in enumerate(legend_items):
    y = legend_y - 0.25 - (i * 0.22)
    # Draw arrow instead of line
    arrow_start = (0.25, y)
    arrow_end = (0.5, y)
    legend_arrow = FancyArrowPatch(arrow_start, arrow_end,
                                  arrowstyle='->', mutation_scale=15,
                                  linewidth=3, color=color, alpha=0.9)
    ax.add_patch(legend_arrow)
    # Add label
    ax.text(0.6, y, label, ha='left', va='center', fontsize=9, color='#333')

# Add color legend for channel emphasis
emphasis_x = 9.5
emphasis_y = 0.8
ax.text(emphasis_x, emphasis_y, 'Channel Emphasis:',
        ha='left', va='center', fontsize=10, fontweight='bold',
        color=COLOR_HIGHLIGHT)

# Primary box and label
prim_box = FancyBboxPatch((emphasis_x, emphasis_y - 0.35), 0.35, 0.18,
                          boxstyle="round,pad=0.02",
                          facecolor=COLOR_PRIMARY, edgecolor='black', linewidth=1.5, alpha=0.7)
ax.add_patch(prim_box)
ax.text(emphasis_x + 0.45, emphasis_y - 0.26, 'Primary', ha='left', va='center', fontsize=9, color='#333')

# Secondary box and label
sec_box = FancyBboxPatch((emphasis_x, emphasis_y - 0.60), 0.35, 0.18,
                         boxstyle="round,pad=0.02",
                         facecolor=COLOR_SECONDARY, edgecolor='black', linewidth=1.5, alpha=0.7)
ax.add_patch(sec_box)
ax.text(emphasis_x + 0.45, emphasis_y - 0.51, 'Secondary', ha='left', va='center', fontsize=9, color='#333')

plt.tight_layout()
plt.savefig('purchase_funnel.png', dpi=300, bbox_inches='tight', facecolor='white')
print("\n✓ Saved: purchase_funnel.png")
plt.close()

print("\n" + "="*80)
print("PURCHASE FUNNEL VISUALIZATION COMPLETE")
print("="*80)
print("\nKey B2B Enterprise Channels:")
print("  • Website/SEO - Organic discovery")
print("  • Industry Events - Trade shows, conferences")
print("  • Case Studies - Customer success stories")
print("  • Demo Requests - Live robot demonstrations")
print("  • Partner Network - System integrators")
print("  • Direct Sales - Enterprise account managers")
print("  • Webinars - Technical education")
print("  • Trade Publications - Industry media")
print("  • LinkedIn B2B - Professional network")
print("  • Email Campaigns - Targeted outreach")
print("  • Pilot Programs - Proof of concept")
print("="*80)
