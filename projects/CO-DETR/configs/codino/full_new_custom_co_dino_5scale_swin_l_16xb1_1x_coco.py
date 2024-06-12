auto_scale_lr = dict(base_batch_size=16, enable=False)
custom_imports = dict(
    allow_failed_imports=False, imports=[
        'projects.CO-DETR.codetr',
    ])
default_hooks = dict(
    checkpoint=dict(
        _scope_='mmdet',
        by_epoch=True,
        interval=1,
        max_keep_ckpts=1,
        type='CheckpointHook'),
    logger=dict(_scope_='mmdet', interval=50, type='LoggerHook'),
    param_scheduler=dict(_scope_='mmdet', type='ParamSchedulerHook'),
    sampler_seed=dict(_scope_='mmdet', type='DistSamplerSeedHook'),
    timer=dict(_scope_='mmdet', type='IterTimerHook'),
    visualization=dict(_scope_='mmdet', type='DetVisualizationHook'))
default_scope = 'mmdet'
env_cfg = dict(
    cudnn_benchmark=False,
    dist_cfg=dict(backend='nccl'),
    mp_cfg=dict(mp_start_method='fork', opencv_num_threads=0))
launcher = 'pytorch'
resume = False # set to true to resume training from previous epoch
#load_from = '/opt/ml/code/checkpoints/epoch_3.pth'
load_from = '/opt/ml/code/work_dirs/custom_co_dino_5scale_swin_l_16xb1_1x_coco/pretrained_model/custom_co_dino_5scale_swin_large_1x_coco-27c13da4.pth'
log_level = 'INFO'
log_processor = dict(
    _scope_='mmdet', by_epoch=True, type='LogProcessor', window_size=50)
loss_lambda = 2.0
max_epochs = 3
max_iters = 270000
metainfo = dict(
    classes=(
        'beetroot-steamed-without-addition-of-salt',
        'bread_wholemeal',
        'jam',
        'water',
        'bread',
        'banana',
        'soft_cheese',
        'ham_raw',
        'hard_cheese',
        'cottage_cheese',
        'coffee',
        'fruit_mixed',
        'pancake',
        'tea',
        'salmon_smoked',
        'avocado',
        'spring_onion_scallion',
        'ristretto_with_caffeine',
        'ham_n_s',
        'egg',
        'bacon',
        'chips_french_fries',
        'juice_apple',
        'chicken',
        'tomato',
        'broccoli',
        'shrimp_prawn',
        'carrot',
        'chickpeas',
        'french_salad_dressing',
        'pasta_hornli_ch',
        'sauce_cream',
        'pasta_n_s',
        'tomato_sauce',
        'cheese_n_s',
        'pear',
        'cashew_nut',
        'almonds',
        'lentil_n_s',
        'mixed_vegetables',
        'peanut_butter',
        'apple',
        'blueberries',
        'cucumber',
        'yogurt',
        'butter',
        'mayonnaise',
        'soup',
        'wine_red',
        'wine_white',
        'green_bean_steamed_without_addition_of_salt',
        'sausage',
        'pizza_margherita_baked',
        'salami_ch',
        'mushroom',
        'tart_n_s',
        'rice',
        'white_coffee',
        'sunflower_seeds',
        'bell_pepper_red_raw',
        'zucchini',
        'asparagus',
        'tartar_sauce',
        'lye_pretzel_soft',
        'cucumber_pickled_ch',
        'curry_vegetarian',
        'soup_of_lentils_dahl_dhal',
        'salmon',
        'salt_cake_ch_vegetables_filled',
        'orange',
        'pasta_noodles',
        'cream_double_cream_heavy_cream_45',
        'cake_chocolate',
        'pasta_spaghetti',
        'black_olives',
        'parmesan',
        'spaetzle',
        'salad_lambs_ear',
        'salad_leaf_salad_green',
        'potato',
        'white_cabbage',
        'halloumi',
        'beetroot_raw',
        'bread_grain',
        'applesauce',
        'cheese_for_raclette_ch',
        'bread_white',
        'curds_natural',
        'quiche',
        'beef_n_s',
        'taboule_prepared_with_couscous',
        'aubergine_eggplant',
        'mozzarella',
        'pasta_penne',
        'lasagne_vegetable_prepared',
        'mandarine',
        'kiwi',
        'french_beans',
        'spring_roll_fried',
        'caprese_salad_tomato_mozzarella',
        'leaf_spinach',
        'roll_of_half_white_or_white_flour_with_large_void',
        'omelette_with_flour_thick_crepe_plain',
        'tuna',
        'dark_chocolate',
        'sauce_savoury_n_s',
        'raisins_dried',
        'ice_tea_on_black_tea_basis',
        'kaki',
        'smoothie',
        'crepe_with_flour_plain',
        'nuggets',
        'chili_con_carne_prepared',
        'veggie_burger',
        'chinese_cabbage',
        'hamburger',
        'soup_pumpkin',
        'sushi',
        'chestnuts_ch',
        'sauce_soya',
        'balsamic_salad_dressing',
        'pasta_twist',
        'bolognaise_sauce',
        'leek',
        'fajita_bread_only',
        'potato_gnocchi',
        'rice_noodles_vermicelli',
        'bread_whole_wheat',
        'onion',
        'garlic',
        'hummus',
        'pizza_with_vegetables_baked',
        'beer',
        'glucose_drink_50g',
        'ratatouille',
        'peanut',
        'cauliflower',
        'green_olives',
        'bread_pita',
        'pasta_wholemeal',
        'sauce_pesto',
        'couscous',
        'sauce',
        'bread_toast',
        'water_with_lemon_juice',
        'espresso',
        'egg_scrambled',
        'juice_orange',
        'braided_white_loaf_ch',
        'emmental_cheese_ch',
        'hazelnut_chocolate_spread_nutella_ovomaltine_caotina',
        'tomme_ch',
        'hazelnut',
        'peach',
        'figs',
        'mashed_potatoes_prepared_with_full_fat_milk_with_butter',
        'pumpkin',
        'swiss_chard',
        'red_cabbage_raw',
        'spinach_raw',
        'chicken_curry_cream_coconut_milk_curry_spices_paste',
        'crunch_muesli',
        'biscuit',
        'meatloaf_ch',
        'fresh_cheese_n_s',
        'honey',
        'vegetable_mix_peas_and_carrots',
        'parsley',
        'brownie',
        'ice_cream_n_s',
        'salad_dressing',
        'dried_meat_n_s',
        'chicken_breast',
        'mixed_salad_chopped_without_sauce',
        'feta',
        'praline_n_s',
        'walnut',
        'potato_salad',
        'kolhrabi',
        'alfa_sprouts',
        'brussel_sprouts',
        'gruyere_ch',
        'bulgur',
        'grapes',
        'chocolate_egg_small',
        'cappuccino',
        'crisp_bread',
        'bread_black',
        'rosti_n_s',
        'mango',
        'muesli_dry',
        'spinach',
        'fish_n_s',
        'risotto',
        'crisps_ch',
        'pork_n_s',
        'pomegranate',
        'sweet_corn',
        'flakes',
        'greek_salad',
        'sesame_seeds',
        'bouillon',
        'baked_potato',
        'fennel',
        'meat_n_s',
        'croutons',
        'bell_pepper_red_stewed',
        'nuts',
        'breadcrumbs_unspiced',
        'fondue',
        'sauce_mushroom',
        'strawberries',
        'pie_plum_baked_with_cake_dough',
        'potatoes_au_gratin_dauphinois_prepared',
        'capers',
        'bread_wholemeal_toast',
        'red_radish',
        'fruit_tart',
        'beans_kidney',
        'sauerkraut',
        'mustard',
        'country_fries',
        'ketchup',
        'pasta_linguini_parpadelle_tagliatelle',
        'chicken_cut_into_stripes_only_meat',
        'cookies',
        'sun_dried_tomatoe',
        'bread_ticino_ch',
        'semi_hard_cheese',
        'porridge_prepared_with_partially_skimmed_milk',
        'juice',
        'chocolate_milk',
        'bread_fruit',
        'corn',
        'dates',
        'pistachio',
        'cream_cheese_n_s',
        'bread_rye',
        'witloof_chicory',
        'goat_cheese_soft',
        'grapefruit_pomelo',
        'blue_mould_cheese',
        'guacamole',
        'tofu',
        'cordon_bleu',
        'quinoa',
        'kefir_drink',
        'salad_rocket',
        'pizza_with_ham_with_mushrooms_baked',
        'fruit_coulis',
        'plums',
        'pizza_with_ham_baked',
        'pineapple',
        'seeds_n_s',
        'focaccia',
        'mixed_milk_beverage',
        'coleslaw_chopped_without_sauce',
        'sweet_potato',
        'chicken_leg',
        'croissant',
        'cheesecake',
        'sauce_cocktail',
        'croissant_with_chocolate_filling',
        'pumpkin_seeds',
        'artichoke',
        'soft_drink_with_a_taste',
        'apple_pie',
        'white_bread_with_butter_eggs_and_milk',
        'savoury_pastry_stick',
        'tuna_in_oil_drained',
        'meat_terrine_pate',
        'falafel_balls',
        'berries_n_s',
        'latte_macchiato',
        'sugar_melon_galia_honeydew_cantaloupe',
        'mixed_seeds_n_s',
        'oil_vinegar_salad_dressing',
        'celeriac',
        'chocolate_mousse',
        'lemon',
        'chocolate_cookies',
        'birchermuesli_prepared_no_sugar_added',
        'muffin',
        'pine_nuts',
        'french_pizza_from_alsace_baked',
        'chocolate_n_s',
        'grits_polenta_maize_flour',
        'wine_rose',
        'cola_based_drink',
        'raspberries',
        'roll_with_pieces_of_chocolate',
        'cake_lemon',
        'rice_wild',
        'gluten_free_bread',
        'pearl_onion',
        'tzatziki',
        'ham_croissant_ch',
        'corn_crisps',
        'lentils_green_du_puy_du_berry',
        'rice_whole_grain',
        'cervelat_ch',
        'aperitif_with_alcohol_n_s_aperol_spritz',
        'peas',
        'tiramisu',
        'apricots',
        'lasagne_meat_prepared',
        'brioche',
        'vegetable_au_gratin_baked',
        'basil',
        'butter_spread_puree_almond',
        'pie_apricot',
        'rusk_wholemeal',
        'pasta_in_conch_form',
        'pasta_in_butterfly_form_farfalle',
        'damson_plum',
        'shoots_n_s',
        'coconut',
        'banana_cake',
        'sauce_curry',
        'watermelon_fresh',
        'white_asparagus',
        'cherries',
        'nectarine',
    ))
model = dict(
    backbone=dict(
        attn_drop_rate=0.0,
        convert_weights=True,
        depths=[
            2,
            2,
            18,
            2,
        ],
        drop_path_rate=0.3,
        drop_rate=0.0,
        embed_dims=192,
        init_cfg=dict(checkpoint='torchvision://resnet50', type='Pretrained'),
        mlp_ratio=4,
        num_heads=[
            6,
            12,
            24,
            48,
        ],
        out_indices=(
            0,
            1,
            2,
            3,
        ),
        patch_norm=True,
        pretrain_img_size=384,
        qk_scale=None,
        qkv_bias=True,
        type='SwinTransformer',
        window_size=12,
        with_cp=False),
    bbox_head=[
        dict(
            anchor_generator=dict(
                octave_base_scale=8,
                ratios=[
                    1.0,
                ],
                scales_per_octave=1,
                strides=[
                    4,
                    8,
                    16,
                    32,
                    64,
                    128,
                ],
                type='AnchorGenerator'),
            bbox_coder=dict(
                target_means=[
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                ],
                target_stds=[
                    0.1,
                    0.1,
                    0.2,
                    0.2,
                ],
                type='DeltaXYWHBBoxCoder'),
            feat_channels=256,
            in_channels=256,
            loss_bbox=dict(loss_weight=24.0, type='GIoULoss'),
            loss_centerness=dict(
                loss_weight=12.0, type='CrossEntropyLoss', use_sigmoid=True),
            loss_cls=dict(
                alpha=0.25,
                gamma=2.0,
                loss_weight=12.0,
                type='FocalLoss',
                use_sigmoid=True),
            num_classes=323,
            stacked_convs=1,
            type='CoATSSHead'),
    ],
    data_preprocessor=dict(
        batch_augments=None,
        bgr_to_rgb=True,
        mean=[
            123.675,
            116.28,
            103.53,
        ],
        pad_mask=False,
        std=[
            58.395,
            57.12,
            57.375,
        ],
        type='DetDataPreprocessor'),
    eval_module='detr',
    neck=dict(
        act_cfg=None,
        in_channels=[
            192,
            384,
            768,
            1536,
        ],
        kernel_size=1,
        norm_cfg=dict(num_groups=32, type='GN'),
        num_outs=5,
        out_channels=256,
        type='ChannelMapper'),
    query_head=dict(
        as_two_stage=True,
        dn_cfg=dict(
            box_noise_scale=1.0,
            group_cfg=dict(dynamic=True, num_dn_queries=100, num_groups=None),
            label_noise_scale=0.5),
        in_channels=2048,
        loss_bbox=dict(loss_weight=5.0, type='L1Loss'),
        loss_cls=dict(
            beta=2.0,
            loss_weight=1.0,
            type='QualityFocalLoss',
            use_sigmoid=True),
        loss_iou=dict(loss_weight=2.0, type='GIoULoss'),
        num_classes=323,
        num_query=900,
        positional_encoding=dict(
            normalize=True,
            num_feats=128,
            temperature=20,
            type='SinePositionalEncoding'),
        transformer=dict(
            decoder=dict(
                num_layers=6,
                return_intermediate=True,
                transformerlayers=dict(
                    attn_cfgs=[
                        dict(
                            dropout=0.0,
                            embed_dims=256,
                            num_heads=8,
                            type='MultiheadAttention'),
                        dict(
                            dropout=0.0,
                            embed_dims=256,
                            num_levels=5,
                            type='MultiScaleDeformableAttention'),
                    ],
                    feedforward_channels=2048,
                    ffn_dropout=0.0,
                    operation_order=(
                        'self_attn',
                        'norm',
                        'cross_attn',
                        'norm',
                        'ffn',
                        'norm',
                    ),
                    type='DetrTransformerDecoderLayer'),
                type='DinoTransformerDecoder'),
            encoder=dict(
                num_layers=6,
                transformerlayers=dict(
                    attn_cfgs=dict(
                        dropout=0.0,
                        embed_dims=256,
                        num_levels=5,
                        type='MultiScaleDeformableAttention'),
                    feedforward_channels=2048,
                    ffn_dropout=0.0,
                    operation_order=(
                        'self_attn',
                        'norm',
                        'ffn',
                        'norm',
                    ),
                    type='BaseTransformerLayer'),
                type='DetrTransformerEncoder',
                with_cp=6),
            num_co_heads=2,
            num_feature_levels=5,
            type='CoDinoTransformer',
            with_coord_feat=False),
        type='CoDINOHead'),
    roi_head=[
        dict(
            bbox_head=dict(
                bbox_coder=dict(
                    target_means=[
                        0.0,
                        0.0,
                        0.0,
                        0.0,
                    ],
                    target_stds=[
                        0.1,
                        0.1,
                        0.2,
                        0.2,
                    ],
                    type='DeltaXYWHBBoxCoder'),
                fc_out_channels=1024,
                in_channels=256,
                loss_bbox=dict(loss_weight=120.0, type='GIoULoss'),
                loss_cls=dict(
                    loss_weight=12.0,
                    type='CrossEntropyLoss',
                    use_sigmoid=False),
                num_classes=323,
                reg_class_agnostic=False,
                reg_decoded_bbox=True,
                roi_feat_size=7,
                type='Shared2FCBBoxHead'),
            bbox_roi_extractor=dict(
                featmap_strides=[
                    4,
                    8,
                    16,
                    32,
                    64,
                ],
                finest_scale=56,
                out_channels=256,
                roi_layer=dict(
                    output_size=7, sampling_ratio=0, type='RoIAlign'),
                type='SingleRoIExtractor'),
            type='CoStandardRoIHead'),
    ],
    rpn_head=dict(
        anchor_generator=dict(
            octave_base_scale=4,
            ratios=[
                0.5,
                1.0,
                2.0,
            ],
            scales_per_octave=3,
            strides=[
                4,
                8,
                16,
                32,
                64,
                128,
            ],
            type='AnchorGenerator'),
        bbox_coder=dict(
            target_means=[
                0.0,
                0.0,
                0.0,
                0.0,
            ],
            target_stds=[
                1.0,
                1.0,
                1.0,
                1.0,
            ],
            type='DeltaXYWHBBoxCoder'),
        feat_channels=256,
        in_channels=256,
        loss_bbox=dict(loss_weight=12.0, type='L1Loss'),
        loss_cls=dict(
            loss_weight=12.0, type='CrossEntropyLoss', use_sigmoid=True),
        type='RPNHead'),
    test_cfg=[
        dict(max_per_img=300, nms=dict(iou_threshold=0.8, type='soft_nms')),
        dict(
            rcnn=dict(
                max_per_img=100,
                nms=dict(iou_threshold=0.5, type='nms'),
                score_thr=0.0),
            rpn=dict(
                max_per_img=1000,
                min_bbox_size=0,
                nms=dict(iou_threshold=0.7, type='nms'),
                nms_pre=1000)),
        dict(
            max_per_img=100,
            min_bbox_size=0,
            nms=dict(iou_threshold=0.6, type='nms'),
            nms_pre=1000,
            score_thr=0.0),
    ],
    train_cfg=[
        dict(
            assigner=dict(
                match_costs=[
                    dict(type='FocalLossCost', weight=2.0),
                    dict(box_format='xywh', type='BBoxL1Cost', weight=5.0),
                    dict(iou_mode='giou', type='IoUCost', weight=2.0),
                ],
                type='HungarianAssigner')),
        dict(
            rcnn=dict(
                assigner=dict(
                    ignore_iof_thr=-1,
                    match_low_quality=False,
                    min_pos_iou=0.5,
                    neg_iou_thr=0.5,
                    pos_iou_thr=0.5,
                    type='MaxIoUAssigner'),
                debug=False,
                pos_weight=-1,
                sampler=dict(
                    add_gt_as_proposals=True,
                    neg_pos_ub=-1,
                    num=512,
                    pos_fraction=0.25,
                    type='RandomSampler')),
            rpn=dict(
                allowed_border=-1,
                assigner=dict(
                    ignore_iof_thr=-1,
                    match_low_quality=True,
                    min_pos_iou=0.3,
                    neg_iou_thr=0.3,
                    pos_iou_thr=0.7,
                    type='MaxIoUAssigner'),
                debug=False,
                pos_weight=-1,
                sampler=dict(
                    add_gt_as_proposals=False,
                    neg_pos_ub=-1,
                    num=256,
                    pos_fraction=0.5,
                    type='RandomSampler')),
            rpn_proposal=dict(
                max_per_img=1000,
                min_bbox_size=0,
                nms=dict(iou_threshold=0.7, type='nms'),
                nms_pre=4000)),
        dict(
            allowed_border=-1,
            assigner=dict(topk=9, type='ATSSAssigner'),
            debug=False,
            pos_weight=-1),
    ],
    type='CoDETR',
    use_lsj=False)
num_dec_layer = 6
optim_wrapper = dict(
    clip_grad=dict(max_norm=0.1, norm_type=2),
    optimizer=dict(lr=1e-04, type='AdamW', weight_decay=0.0001),
    paramwise_cfg=dict(custom_keys=dict(backbone=dict(lr_mult=0.1))),  # resulting lr: 1e-5
    type='OptimWrapper')
param_scheduler = [
    dict(
        begin=0, by_epoch=False, end=250, start_factor=0.001, type='LinearLR'),
]
test_cfg = dict(_scope_='mmdet', type='TestLoop')
test_dataloader = dict(
    batch_size=1,
    dataset=dict(
        _scope_='mmdet',
        ann_file='/root/Sofia/Genioos/data/full_dataset/test/test.json',
        backend_args=None,
        data_prefix=dict(
            img='/root/Sofia/Genioos/data/full_dataset/test/images/'),
        data_root='/root/Sofia/Genioos/data/full_dataset/',
        pipeline=[
            dict(backend_args=None, type='LoadImageFromFile'),
            dict(keep_ratio=True, scale=(
                1333,
                800,
            ), type='Resize'),
            dict(type='LoadAnnotations', with_bbox=True),
            dict(
                meta_keys=(
                    'img_id',
                    'img_path',
                    'ori_shape',
                    'img_shape',
                    'scale_factor',
                ),
                type='PackDetInputs'),
        ],
        test_mode=True,
        type='Coco323Dataset'),
    drop_last=False,
    num_workers=2,
    persistent_workers=True,
    sampler=dict(_scope_='mmdet', shuffle=False, type='DefaultSampler'))
test_evaluator = dict(
    _scope_='mmdet',
    ann_file='/root/Sofia/Genioos/data/full_dataset/test/test.json',
    backend_args=None,
    format_only=False,
    metric='bbox',
    type='CocoMetric')
test_pipeline = [
    dict(backend_args=None, type='LoadImageFromFile'),
    dict(keep_ratio=True, scale=(
        1333,
        800,
    ), type='Resize'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(
        meta_keys=(
            'img_id',
            'img_path',
            'ori_shape',
            'img_shape',
            'scale_factor',
        ),
        type='PackDetInputs'),
]
total_epochs = 3
train_cfg = dict(max_epochs=3, type='EpochBasedTrainLoop', val_interval=1)
train_dataloader = dict(
    batch_size=1,
    dataset=dict(
        ann_file='/opt/ml/input/data/train/correct_train.json',
        backend_args=None,
        data_prefix=dict(img='/opt/ml/input/data/train/images/'),
        data_root='/opt/ml/input/data/',
        filter_cfg=dict(filter_empty_gt=False, min_size=32),
        pipeline=[
            dict(backend_args=None, type='LoadImageFromFile'),
            dict(type='LoadAnnotations', with_bbox=True),
            dict(prob=0.5, type='RandomFlip'),
            dict(
                transforms=[
                    [
                        dict(
                            keep_ratio=True,
                            scales=[
                                (
                                    480,
                                    1333,
                                ),
                                (
                                    512,
                                    1333,
                                ),
                                (
                                    544,
                                    1333,
                                ),
                                (
                                    576,
                                    1333,
                                ),
                                (
                                    608,
                                    1333,
                                ),
                                (
                                    640,
                                    1333,
                                ),
                                (
                                    672,
                                    1333,
                                ),
                                (
                                    704,
                                    1333,
                                ),
                                (
                                    736,
                                    1333,
                                ),
                                (
                                    768,
                                    1333,
                                ),
                                (
                                    800,
                                    1333,
                                ),
                            ],
                            type='RandomChoiceResize'),
                    ],
                    [
                        dict(
                            keep_ratio=True,
                            scales=[
                                (
                                    400,
                                    4200,
                                ),
                                (
                                    500,
                                    4200,
                                ),
                                (
                                    600,
                                    4200,
                                ),
                            ],
                            type='RandomChoiceResize'),
                        dict(
                            allow_negative_crop=True,
                            crop_size=(
                                384,
                                600,
                            ),
                            crop_type='absolute_range',
                            type='RandomCrop'),
                        dict(
                            keep_ratio=True,
                            scales=[
                                (
                                    480,
                                    1333,
                                ),
                                (
                                    512,
                                    1333,
                                ),
                                (
                                    544,
                                    1333,
                                ),
                                (
                                    576,
                                    1333,
                                ),
                                (
                                    608,
                                    1333,
                                ),
                                (
                                    640,
                                    1333,
                                ),
                                (
                                    672,
                                    1333,
                                ),
                                (
                                    704,
                                    1333,
                                ),
                                (
                                    736,
                                    1333,
                                ),
                                (
                                    768,
                                    1333,
                                ),
                                (
                                    800,
                                    1333,
                                ),
                            ],
                            type='RandomChoiceResize'),
                    ],
                ],
                type='RandomChoice'),
            dict(type='PackDetInputs'),
        ],
        type='Coco323Dataset'),
    num_workers=1,
    persistent_workers=True,
    sampler=dict(_scope_='mmdet', shuffle=True, type='DefaultSampler'))
train_pipeline = [
    dict(backend_args=None, type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(prob=0.5, type='RandomFlip'),
    dict(
        transforms=[
            [
                dict(
                    keep_ratio=True,
                    scales=[
                        (
                            480,
                            1333,
                        ),
                        (
                            512,
                            1333,
                        ),
                        (
                            544,
                            1333,
                        ),
                        (
                            576,
                            1333,
                        ),
                        (
                            608,
                            1333,
                        ),
                        (
                            640,
                            1333,
                        ),
                        (
                            672,
                            1333,
                        ),
                        (
                            704,
                            1333,
                        ),
                        (
                            736,
                            1333,
                        ),
                        (
                            768,
                            1333,
                        ),
                        (
                            800,
                            1333,
                        ),
                    ],
                    type='RandomChoiceResize'),
            ],
            [
                dict(
                    keep_ratio=True,
                    scales=[
                        (
                            400,
                            4200,
                        ),
                        (
                            500,
                            4200,
                        ),
                        (
                            600,
                            4200,
                        ),
                    ],
                    type='RandomChoiceResize'),
                dict(
                    allow_negative_crop=True,
                    crop_size=(
                        384,
                        600,
                    ),
                    crop_type='absolute_range',
                    type='RandomCrop'),
                dict(
                    keep_ratio=True,
                    scales=[
                        (
                            480,
                            1333,
                        ),
                        (
                            512,
                            1333,
                        ),
                        (
                            544,
                            1333,
                        ),
                        (
                            576,
                            1333,
                        ),
                        (
                            608,
                            1333,
                        ),
                        (
                            640,
                            1333,
                        ),
                        (
                            672,
                            1333,
                        ),
                        (
                            704,
                            1333,
                        ),
                        (
                            736,
                            1333,
                        ),
                        (
                            768,
                            1333,
                        ),
                        (
                            800,
                            1333,
                        ),
                    ],
                    type='RandomChoiceResize'),
            ],
        ],
        type='RandomChoice'),
    dict(type='PackDetInputs'),
]
val_cfg = dict(_scope_='mmdet', type='ValLoop')
val_dataloader = dict(
    batch_size=1,
    dataset=dict(
        _scope_='mmdet',
        ann_file='/opt/ml/input/data/validation/correct_val.json',
        backend_args=None,
        data_prefix=dict(img='/opt/ml/input/data/validation/images/'),
        data_root='/opt/ml/input/data/',
        pipeline=[
            dict(backend_args=None, type='LoadImageFromFile'),
            dict(keep_ratio=True, scale=(
                1333,
                800,
            ), type='Resize'),
            dict(type='LoadAnnotations', with_bbox=True),
            dict(
                meta_keys=(
                    'img_id',
                    'img_path',
                    'ori_shape',
                    'img_shape',
                    'scale_factor',
                ),
                type='PackDetInputs'),
        ],
        test_mode=True,
        type='Coco323Dataset'),
    drop_last=False,
    num_workers=2,
    persistent_workers=True,
    sampler=dict(_scope_='mmdet', shuffle=False, type='DefaultSampler'))
val_evaluator = dict(
    _scope_='mmdet',
    ann_file='/opt/ml/input/data/validation/correct_val.json',
    backend_args=None,
    format_only=False,
    metric='bbox',
    type='CocoMetric')
vis_backends = [
    dict(_scope_='mmdet', type='LocalVisBackend'),
]
visualizer = dict(
    _scope_='mmdet',
    name='visualizer',
    type='DetLocalVisualizer',
    vis_backends=[
        dict(_scope_='mmdet', type='LocalVisBackend'),
    ])
work_dir = '/opt/ml/checkpoints'
